import math
from config import DISPLAY_W, DISPLAY_H
from player import Player
from enemy import Enemy
from colissions import isCollision
import pygame
from menu import *
from games.game import Game

class Cars(Game):
    def __init__(self):
        Game.__init__(self)
        self.playing = True
        
    def game_loop(self):
        player = Player()
        enemies = list()
        enemies.append(Enemy())
        framecounter = 0

        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False

            self.display.fill(self.WHITE)

            # BOUNDARIES
            pygame.draw.rect(
                self.display,
                (self.BLACK),
                (0, 0, self.DISPLAY_W * (self.Boundaries_L_R_U_D[0]), self.DISPLAY_H),
                0,
            )
            pygame.draw.rect(
                self.display,
                (self.BLACK),
                (
                    self.DISPLAY_W * (self.Boundaries_L_R_U_D[1]),
                    0,
                    self.DISPLAY_W,
                    self.DISPLAY_H,
                ),
                0,
            )

            # Player
            player.movement(self)
            player.draw(self.display)
            player.rect = player.ship.get_rect(topleft=(player.position_X, player.position_Y))
            self.display.blit(player.ship, player.rect)

            # This is much better - not depended on lags
            framecounter += 1
            if framecounter == 1000:
                enemies.append(Enemy())
                framecounter = 0

            for e in enemies:
                e.draw(self.display)
                e.rect = e.ship.get_rect(topleft=(e.position_X, e.position_Y))
                if isCollision(player.rect, e.rect):
                    enemies.remove(e)
                elif e.get_coordinates()[1] > self.DISPLAY_H:
                    print("gone")
                    enemies.remove(e)

            # Finalize

            # self.window.blit("XXXXXX", (0,0))
            # x = clock.get_fps()
            self.window.blit(self.display, (0, 0))
            # self.window.blit(self.update_fps(start, self.font), (self.DISPLAY_W - 200, self.DISPLAY_H / 2 - 20))

            pygame.display.update()
            # self.reset_keys()       