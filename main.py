import pygame
from menus.menu_choices import *


from games.game import Game
from games.cars import Cars
from games.cars_x_y import Cars_X_Y
from menus.menu_runner import Menu_Runner
from games.space_rocket import Space_Rocket

games_by_id =  {1: Cars(), 2: Cars_X_Y(), 3: Space_Rocket()}


if __name__ == "__main__":
    runner = Menu_Runner()
    pygame.mixer.init()
    pygame.mixer.music.load("music/morgantj_-_I_m_Going_Bazurky.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(runner.music_volume)

    while runner.running:
        runner.curr_menu.display_menu()
        if runner.start_the_game == True:
            runner.start_the_game = False
            current = runner.curr_menu.current_level
            try:
                game = games_by_id[current]
                game.game_loop()
                game.reset_keys()
            except KeyError:
                print("No such a game yet")
