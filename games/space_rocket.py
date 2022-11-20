import math
from config import DISPLAY_W, DISPLAY_H
from player import Player
from enemies.cars_enemy import Cars_Enemy
from colissions import isCollision
import pygame
from menus.menu_choices import *
from games.game import Game
from objects.life_counter import Heart

pygame.init()
basic_font = pygame.font.SysFont("Arial", 18)


class Space_Rocket(Game):
    def __init__(self):
        Game.__init__(self)
        self.playing = True
        self.Boundaries_L_R_U_D = [0,1,1,0]
 
    def move_player(self, player):
        # player.movement_X(self)
        player.movement_X_drift(self)
        player.movement_Y(self)
        
    def game_loop(self):
        player = Player((2,2))
        enemies = list()
        enemies.append(Cars_Enemy())
        framecounter = 0
        lifes = Heart(3)
        self.playing = True

        while self.playing:
            self.check_events()

            if self.START_KEY:
                self.playing = False
            self.display.fill(self.WHITE)


            # Player
            self.move_player(player)
            # player.movement(self)
            player.draw(self.display)
            player.rect = player.ship.get_rect(topleft=(player.position_X, player.position_Y))
            self.display.blit(player.ship, player.rect)

            # This is much better - not depended on lags
            framecounter += 1
            if framecounter == 200:
                enemies.append(Cars_Enemy())
                framecounter = 0

            # for e in enemies:
            #     e.draw(self.display)
            #     e.rect = e.ship.get_rect(topleft=(e.position_X, e.position_Y))
            #     if isCollision(player.rect, e.rect):
            #         enemies.remove(e)
            #         lifes.lifes -= 1
            #     elif e.get_coordinates()[1] > self.DISPLAY_H:
            #         self.score += 1
            #         enemies.remove(e)
                    
            lifes.draw(self.display)
            # self.draw_text(str(self.score), 30, self.DISPLAY_W - self.DISPLAY_W/10, self.DISPLAY_H/10)

            # Finalize
            if lifes.lifes <= 0:
                self.playing = False
           
            self.window.blit(self.display, (0, 0))
            
            self.window.blit(self.update_fps(), (10,0))
            self.clock.tick(240)

            pygame.display.update()