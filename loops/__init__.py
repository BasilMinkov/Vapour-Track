import pygame
import os

from inlets.lsl_inlet import LSLInlet
from static_variables import DISPLAY_WIDTH, DISPLAY_HIGHT, STATIC_PATH


class Loop:

    def __init__(self, game):
        self.game = game

    def render(self):
        pygame.display.update()

    def handle_events(self):
        pass

    def set_lsl(self):
        if self.game.params.control == "BCI":
            self.lsl = LSLInlet(name='NFBLab_data')
            state = 0

    def text_object(self, text, font):
        """ Returns PyGame text object and it's size """
        TextSurface = font.render(text, True, (250, 0, 0))
        return TextSurface, TextSurface.get_rect()

    def message_display(self, text):
        """ Makes a text message in the center of a screen """
        largeText = pygame.font.Font(os.path.join(STATIC_PATH, "9921.otf"), 90)
        TextSurf, TextRect = self.text_object(text, largeText)
        TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HIGHT / 2))
        self.game.params.gameDisplay.blit(TextSurf, TextRect)
