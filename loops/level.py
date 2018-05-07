import os
import random
import time
import pygame
import numpy as np

from loops import Loop
from static_variables import DISPLAY_HIGHT, DISPLAY_WIDTH, WHITE, STATIC_PATH, BLACK
from inlets.utils import QuantileSmoother


class Level(Loop):

    def __init__(self, game):

        super().__init__(game)

        self.background_img_3_hight = game.static.background_img_3.get_rect().size[1]
        running = True

        self.square = BLACK

        self.oscillation = False
        self.x = DISPLAY_WIDTH * 0.45  # OX spacecraft start position
        self.y = DISPLAY_HIGHT * 0.5  # OY spacecraft start position
        self.y_deviation = DISPLAY_HIGHT / 2
        self.timer = 0
        self.BCI_timer = 0
        self.k = 0.7
        self.fuel = 0
        self.amplitude = 0
        self.parallax = 0
        self.spacecraft_state = 2
        self.flame_wait = 0
        self.noise = -2
        self.noise_state = 0
        self.waiting_time = 3
        self.set_lsl()
        self.trail = "Real"

        while running:

            game.params.clock.tick(60)  # frames per second
            self.timer += 0.1
            self.handle_events()
            self.render()

    def handle_flame(self):
        if self.fuel == 0:
            self.spacecraft_state = 2
        if self.fuel > 0:
            if self.flame_wait >= 0:
                self.spacecraft_state = 0
            if self.flame_wait >= 5:
                self.spacecraft_state = 1
            if self.flame_wait >= 10:
                self.flame_wait = -1
            self.flame_wait += 1

    def update_noise(self):

        if self.noise_state == 0:
            if self.noise < 5:
                self.noise += 0.25
            else:
                self.noise_state = 1
        elif self.noise_state == 1:
            if self.noise > -5:
                self.noise -= 0.25
            else:
                self.noise_state = 0

    def handle_events(self):

        if time.time() - self.BCI_timer > self.waiting_time - 2:
            self.square = BLACK
        else:
            self.square = WHITE

        # Every iteration

        self.handle_flame()
        self.update_noise()

        if self.fuel != 0:
            self.oscillation = False
            self.y_deviation -= 5
            self.fuel -= 10
            self.parallax += 5
        elif self.fuel == 0:
            if self.oscillation is False:
                self.amplitude = self.y_deviation
                self.timer = 0
                self.oscillation = True

        if self.oscillation is True:
            self.y_deviation = self.amplitude * np.exp(-self.k * self.timer) * np.cos(self.timer * np.pi / 2)

        # Control

        for event in pygame.event.get():  # list of events per t
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_UP:
                    self.fuel = 150

        if self.game.params.control == "BCI":
            chunk = self.lsl.get_next_chunk()[0]
            fs = self.lsl.get_frequency()
            smoother = QuantileSmoother(fs * 10, 0.92)
            threshold = smoother.apply(chunk)
            print(chunk)
            if chunk is not None:
                if time.time() - self.BCI_timer > self.waiting_time:
                    if self.trail == "Real":
                        if max(chunk[:, 0]) > threshold[-1]:
                            self.fuel = 150
                            self.BCI_timer = time.time()
                    else:
                        if max(chunk[:, 2]) > max(chunk[:, 5]):
                            self.fuel = 150
                            self.BCI_timer = time.time()

            # if chunk is not None:
            #     if time.time() - self.BCI_timer > self.waiting_time:
            #         if False:  # TODO True is Real FB, False is Mock
            #             if max(chunk[:, 0]) > max(chunk[:, 4]):
            #                 self.fuel = 150
            #                 self.flash = True
            #                 self.BCI_timer = time.time()
            #         else:
            #             if max(chunk[:, 2]) > max(chunk[:, 5]):
            #                 self.fuel = 150
            #                 self.flash = True
            #                 self.BCI_timer = time.time()

    def render(self):
        y_deviation = - self.background_img_3_hight + DISPLAY_HIGHT + self.parallax + self.noise
        self.game.params.gameDisplay.blit(self.game.static.background_img_3, (0 + self.noise, 0 + y_deviation))
        self.spacecraft(self.game.static.spacecraft_img_list[self.spacecraft_state], self.x, self.y + self.y_deviation)

        # if self.square:
        #     pygame.draw.rect(self.game.params.gameDisplay, WHITE, (DISPLAY_WIDTH-100, 0, 100, 100))
        # else:
        pygame.draw.rect(self.game.params.gameDisplay, self.square, (DISPLAY_WIDTH-100, 0, 100, 100))

        # self.show_statistics()
        super().render()

    def spacecraft(self, img, x, y):
        self.game.params.gameDisplay.blit(img, (x, y))

    def ring(self, coinX, coinY, coin_size, img):
        img = pygame.transform.scale(img, (coin_size, coin_size))
        self.game.params.gameDisplay.blit(img, (coinX, coinY))

    def show_statistics(self):
        font = pygame.font.Font(os.path.join(STATIC_PATH, "9921.otf"), 25)
        text = font.render('flamewait: {}, spacecraftstate: {}'.format(str(self.flame_wait), str(self.spacecraft_state)), True, WHITE)
        self.game.params.gameDisplay.blit(text, (5, 0))