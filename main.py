import pygame
from menu import *


from games.game import Game
from games.cars import Cars

games_by_id =  {1: Cars()}


if __name__ == "__main__":
    g = Game()
    pygame.mixer.init()
    pygame.mixer.music.load("music/morgantj_-_I_m_Going_Bazurky.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(g.music_volume)

    while g.running:
        g.curr_menu.display_menu()

        if g.playing == True:
            current = g.curr_menu.current_level
            try:
                game = games_by_id[current]
                game.game_loop()
            except KeyError:
                print("No such a game yet")
