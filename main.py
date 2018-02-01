import sys
import os
import pygame
import numpy as np
import random
import time

STATIC_PATH = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/static')
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1440, 900

print(STATIC_PATH)


class Parameters:

    def __init__(self):

        self.running = True

        # Initialise pygame
        pygame.init()
        pygame.mixer.init()
        self.running = True

        # Initialise display
        pygame.display.set_caption("Vapour Track")
        self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT),
                                                   (pygame.FULLSCREEN | pygame.HWSURFACE))
        self.clock = pygame.time.Clock()

        # Load static
        self.static = Loader()


class Game:

    def __init__(self):
        random.seed(time.time())

        # Set system game parameters
        params = Parameters()

        # Game modules sequence
        Sequence()

        # End of program
        pygame.quit()
        quit()


class Sequence:

    def __init__(self):
        Menu()


class Loader:

    def __init__(self):
        # loading sounds
        self.sound_soundtrack = self.load_sound('soundtrack.wav')
        self.sound_beep = self.load_sound('Beep17.wav')
        self.sound_change = self.load_sound('change.wav')
        self.sound_returns = self.load_sound('return.wav')

        # loading spacecraft image
        self.spacecraft_move1_img = self.load_image('spacecraft_2.png')
        self.spacecraft_stop_img = self.load_image('spacecraft_3.png')
        self.spacecraft_size = (150, 150)
        self.spacecraft_move0_img = pygame.transform.scale(self.load_image('spacecraft.png'), self.spacecraft_size)
        self.spacecraft_move1_img = pygame.transform.scale(self.load_image('spacecraft_2.png'), self.spacecraft_size)
        self.spacecraft_stop_img = pygame.transform.scale(self.load_image('spacecraft_3.png'), self.spacecraft_size)

        # loading background image
        self.background_img = self.load_image('background.jpg')

    @staticmethod
    def load_image(name):
        """ Load image and return image object. """
        fullname = os.path.join(STATIC_PATH, 'images', name)
        image = pygame.image.load(fullname)
        return image

    @staticmethod
    def load_sound(name):
        """ Load sound and return sound object. """
        fullname = os.path.join(STATIC_PATH, 'sounds', name)
        sound = pygame.mixer.Sound(fullname)
        return sound


class Loop:

    def __init__(self):
        pass

    def message_center_display(self, text, x, y):
        """ Makes a text message in the center of a screen """
        largeText = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 90)
        TextSurf, TextRect = self.text_object(text, largeText)
        TextRect.center = (x, y)
        game.gameDisplay.blit(TextSurf, TextRect)

    @staticmethod
    def text_object(text, font):
        """ Returns PyGame text object and it's size """
        TextSurface = font.render(text, True, (0, 0, 0))
        return TextSurface, TextSurface.get_rect()


class Menu(Loop):

    def __init__(self):

        super().__init__()

        intro = True

        self.background_img_hight = game.static.background_img.get_rect().size[1]

        # menu states: 0 - new game; 1 - continue; 2 - settings; 3 - exit.
        menu_id = 0

        while intro:

            game_window.clock.tick(60)

            game_window.gameDisplay.blit(game.static.background_img, (0, (0 - self.background_img_hight)))
            game_window.gameDisplay.blit(game.static.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(self.static.change)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_DOWN:
                        if menu_id < 4:
                            menu_id += 1
                        if menu_id == 4:
                            menu_id = 0
                    if event.key == pygame.K_UP:
                        if menu_id == -1:
                            menu_id = 3
                        if menu_id > -1:
                            menu_id -= 1
                    if event.key == pygame.K_RETURN and menu_id == 0:
                        # game_loop()
                        pass

            # game.gameDisplay.blit(menu[menu_id], (0, 0))
            pygame.display.update()


# class SetUp:
#
#     def __init__(self):
#         pass
#
#
# class Level:
#
#     def __init__(self):
#
#         backgroundImgHight = backgroundImg.get_rect().size[1]
#
#         x = DISPLAY_WIDTH * 0.45  # OX spacecraft start position
#         y = DISPLAY_HEIGHT * 0.8  # OY spacecraft start position
#
#         x_change = 0
#
#         coin = coins[0]
#         coin_size = 65
#         coin_startX = random.randrange(500, DISPLAY_WIDTH - 500)
#         coin_startY = -200
#         coin_speed = 5
#
#         planet = planets[0]
#         planet_size = 500
#         planet_startX = random.randrange(-300, DISPLAY_WIDTH - 300)
#         planet_startY = -600
#         planet_speed = 1
#
#         gameExit = False
#         speed_up = False
#
#         score = 0
#         distance = 0
#         counter = 0
#         coin_state = 1
#         parallax = 0
#         sps = 0
#         boost = 0
#         delayB = 0
#         delayM = 0
#         delayP = 0
#
#         pygame.mixer.Sound.play(soundtrack, loops=-1)
#
#         while not gameExit:
#
#             clock.tick(60)  # frames per second
#             parallax += 3
#             parallax += boost
#             if parallax >= backgroundImgHight:
#                 parallax = 0
#
#             for event in pygame.event.get():  # list of events per t
#
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_ESCAPE:
#                         pygame.quit()
#                         quit()
#                     if event.key == pygame.K_LEFT:
#                         x_change = -20
#                     if event.key == pygame.K_RIGHT:
#                         x_change = 20
#
#                 if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                         x_change = 0
#
#             x += x_change
#
#             gameDisplay.blit(backgroundImg, (0, 0 - backgroundImgHight + parallax))
#             gameDisplay.blit(backgroundImg, (0, 0 + parallax))
#
#             counter += 1
#
#             if counter > 10:
#                 counter = 0
#
#             # ring(planet_startX, planet_startY, planet_size, planet)
#             ring(coin_startX, coin_startY, coin_size, coin)
#             coin_startY += coin_speed + boost
#             # planet_startY += planet_speed+boost
#             distance += 1 + boost
#             demons_dodged(score, distance)
#
#             if counter > 5:
#                 spacecraft(spacecraftImg, x, y)
#             else:
#                 spacecraft(spacecraft2Img, x, y)
#
#             if x > DISPLAY_WIDTH - spacecraft_width or x < 0:
#                 pygame.mixer.Sound.stop(soundtrack)
#                 pygame.mixer.Sound.play(returns)
#                 crash(explosion_1, explosion_2, backgroundImg, parallax, x, y)
#
#             if coin_startY > DISPLAY_HEIGHT:
#                 coin_startY = -coin_size
#                 coin_startX = random.randrange(50, DISPLAY_WIDTH - 50)
#
#             if planet_startY > DISPLAY_HEIGHT:
#                 planet = planets[random.randrange(len(planets))]
#                 planet_startY = -planet_size
#                 planet_startX = random.randrange(500, DISPLAY_WIDTH - 500)
#
#             if coin_state < 10:
#                 coin = coins[0]
#             elif 10 <= coin_state < 20:
#                 coin = coins[1]
#             elif 20 <= coin_state < 30:
#                 coin = coins[2]
#             elif 30 <= coin_state < 40:
#                 coin = coins[3]
#
#             coin_state += 1
#             if coin_state >= 40:
#                 coin_state = 1
#
#             if y <= coin_startY + coin_size:
#                 if x > coin_startX and x < coin_startX + coin_size or x + spacecraft_width > coin_startX and x + spacecraft_width < coin_startX + coin_size or x < coin_startX and x + spacecraft_width > coin_startX + coin_size:
#                     pygame.mixer.Sound.play(beep)
#                     coin_startY = -coin_size
#                     coin_startX = random.randrange(500, display_width - 500)
#                     # crash(explosion_1, explosion_2, backgroundImg, parallax, x, y)
#                     score += 1
#                     speed_up = True
#
#             if speed_up == True:
#                 sps += 5
#                 # delayB = 30
#                 speed_up = False
#
#             if sps > 0 and delayP == 0:
#                 boost += 1
#                 sps -= 1
#                 delayP = 0
#             elif sps > 0:
#                 delayP -= 1
#
#             if sps == 0 and boost > 0 and delayM == 0:
#                 boost -= 1
#                 delayM = 10
#             if sps == 0 and boost > 0:
#                 delayM -= 1
#
#             if boost > 30:
#                 boost = 30
#
#             pygame.display.update()  # .flip()
#
#     def demons_dodged(count, distance):
#         font = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 25)
#         text = font.render('Scores: {}, Distance: {} km'.format(str(count), str(distance)), True, white)
#         gameDisplay.blit(text, (5, 0))
#
#
#
# class Player:
#
#     def __init__(self):
#         pass


# Essentials


# Characters


# def spacecraft(img, x, y):
#     gameDisplay.blit(img, (x, y))
#
#
# def ring(coinX, coinY, coin_size, img):
#     img = pygame.transform.scale(img, (coin_size, coin_size))
#     gameDisplay.blit(img, (coinX, coinY))
#
#
# # Passive Loops
#
#
# def crash(img1, img2, bg, c, x, y):
#     for i in range(3):
#         message_display('GAME OVER!')
#         pygame.time.wait(200)
#         gameDisplay.blit(img1, (x, y))
#         pygame.display.update()
#
#         pygame.time.wait(200)
#         gameDisplay.blit(bg, (0, 0 + c))
#         gameDisplay.blit(img2, (x, y))
#         message_display('GAME OVER!')
#         pygame.display.update()
#
#         gameDisplay.blit(bg, (0, 0 + c))
#     game_loop()
#
#
# # Active Loops
#
# def game_loop():
#     backgroundImgHight = backgroundImg.get_rect().size[1]
#
#     x = display_width * 0.45  # OX spacecraft start position
#     y = display_hight * 0.8  # OY spacecraft start position
#
#     x_change = 0
#
#     coin = coins[0]
#     coin_size = 65
#     coin_startX = random.randrange(500, display_width - 500)
#     coin_startY = -200
#     coin_speed = 5
#
#     planet = planets[0]
#     planet_size = 500
#     planet_startX = random.randrange(-300, display_width - 300)
#     planet_startY = -600
#     planet_speed = 1
#
#     gameExit = False
#     speed_up = False
#
#     score = 0
#     distance = 0
#     counter = 0
#     coin_state = 1
#     parallax = 0
#     sps = 0
#     boost = 0
#     delayB = 0
#     delayM = 0
#     delayP = 0
#
#     pygame.mixer.Sound.play(soundtrack, loops=-1)
#
#     while not gameExit:
#
#         clock.tick(60)  # frames per second
#         parallax += 3
#         parallax += boost
#         if parallax >= backgroundImgHight:
#             parallax = 0
#
#         for event in pygame.event.get():  # list of events per t
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     quit()
#                 if event.key == pygame.K_LEFT:
#                     x_change = -20
#                 if event.key == pygame.K_RIGHT:
#                     x_change = 20
#
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0
#
#         x += x_change
#
#         gameDisplay.blit(backgroundImg, (0, 0 - backgroundImgHight + parallax))
#         gameDisplay.blit(backgroundImg, (0, 0 + parallax))
#
#         counter += 1
#
#         if counter > 10:
#             counter = 0
#
#         # ring(planet_startX, planet_startY, planet_size, planet)
#         ring(coin_startX, coin_startY, coin_size, coin)
#         coin_startY += coin_speed + boost
#         # planet_startY += planet_speed+boost
#         distance += 1 + boost
#         demons_dodged(score, distance)
#
#         if counter > 5:
#             spacecraft(spacecraftImg, x, y)
#         else:
#             spacecraft(spacecraft2Img, x, y)
#
#         if x > display_width - spacecraft_width or x < 0:
#             pygame.mixer.Sound.stop(soundtrack)
#             pygame.mixer.Sound.play(returns)
#             crash(explosion_1, explosion_2, backgroundImg, parallax, x, y)
#
#         if coin_startY > display_hight:
#             coin_startY = -coin_size
#             coin_startX = random.randrange(50, display_width - 50)
#
#         if planet_startY > display_hight:
#             planet = planets[random.randrange(len(planets))]
#             planet_startY = -planet_size
#             planet_startX = random.randrange(500, display_width - 500)
#
#         if coin_state < 10:
#             coin = coins[0]
#         elif 10 <= coin_state < 20:
#             coin = coins[1]
#         elif 20 <= coin_state < 30:
#             coin = coins[2]
#         elif 30 <= coin_state < 40:
#             coin = coins[3]
#
#         coin_state += 1
#         if coin_state >= 40:
#             coin_state = 1
#
#         if y <= coin_startY + coin_size:
#             if x > coin_startX and x < coin_startX + coin_size or x + spacecraft_width > coin_startX and x + spacecraft_width < coin_startX + coin_size or x < coin_startX and x + spacecraft_width > coin_startX + coin_size:
#                 pygame.mixer.Sound.play(beep)
#                 coin_startY = -coin_size
#                 coin_startX = random.randrange(500, display_width - 500)
#                 # crash(explosion_1, explosion_2, backgroundImg, parallax, x, y)
#                 score += 1
#                 speed_up = True
#
#         if speed_up == True:
#             sps += 5
#             # delayB = 30
#             speed_up = False
#
#         if sps > 0 and delayP == 0:
#             boost += 1
#             sps -= 1
#             delayP = 0
#         elif sps > 0:
#             delayP -= 1
#
#         if sps == 0 and boost > 0 and delayM == 0:
#             boost -= 1
#             delayM = 10
#         if sps == 0 and boost > 0:
#             delayM -= 1
#
#         if boost > 30:
#             boost = 30
#
#         pygame.display.update()  # .flip()


# loading title image

game = Game()
