import pygame

from static_variables import DISPLAY_HIGHT, DISPLAY_WIDTH
from loops import Loop
from loops.level import Level
from system.loader import Loader


class Menu(Loop):

    def __init__(self, game):

        super().__init__(game)

        intro = True

        background_img_3_hight = game.static.background_img_3.get_rect().size[1]
        print("Background image 3 hight: ", background_img_3_hight)
        planet = Loader.load_image('p1.png')

        menu = [game.static.new_game,
                game.static.load_game,
                game.static.settings,
                game.static.credits]

        menu_id = 0

        while intro:

            game.params.clock.tick(60)

            game.params.gameDisplay.blit(game.static.background_img_3, (0, 0-background_img_3_hight+DISPLAY_HIGHT))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(game.static.change)
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
                    if event.key == pygame.K_RETURN:
                        if menu_id == 0:
                            Level(game)
                        elif menu_id == 2:
                            from loops.settings import Settings
                            Settings(game)

            game.params.gameDisplay.blit(game.static.title_1, (0, 0))

            game.params.gameDisplay.blit(menu[menu_id], (0, 0))
            pygame.display.update()
