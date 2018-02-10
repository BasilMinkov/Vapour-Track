import pygame

from system.loader import Loader
from system.parameters import Parameters
from loops.menu import Menu


class Game:
    def __init__(self):
        # Load game system parameters
        self.params = Parameters()

        # Load static objects (images, sounds)
        self.static = Loader()

    def run(self):
        pygame.mixer.Sound.play(game.static.soundtrack, loops=-1)
        Menu(self)


if __name__ == "__main__":
    game = Game()
    game.run()
