import math
from config import DISPLAY_W, DISPLAY_H
# from player import Player
# from enemy import Enemy
# from colissions import isCollision
import pygame
from menus.menu_choices import *
from pathlib import Path
fonts_folder = Path("fonts")


class Game:

    def __init__(self) -> None:
        pygame.init()
        
        self.basic_font = pygame.font.SysFont("Arial", 18)

        self.clock = pygame.time.Clock()

        self.Boundaries_L_R_U_D = [2 / 6, 4 / 6, 1, 0]
        self.playing = False
        (
            self.UP_KEY,
            self.DOWN_KEY,
            self.START_KEY,
            self.BACK_KEY,
            self.LEFT_KEY,
            self.RIGHT_KEY,
        ) = (False, False, False, False, False, False)
        self.DISPLAY_W = DISPLAY_W
        self.DISPLAY_H = DISPLAY_H
        self.DISPLAY_SIZE = (self.DISPLAY_W, self.DISPLAY_H)
        self.display = pygame.Surface(self.DISPLAY_SIZE)
        self.window = pygame.display.set_mode((self.DISPLAY_SIZE))
        self.font_name  = fonts_folder / "PixeloidMono-1G8ae.ttf"

 
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.music_volume = 0.1
        self.font = pygame.font.Font(self.font_name, 10)
        
        self.score = 0
        self.lifes = 3

    def update_fps(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = self.basic_font.render(fps, 1, pygame.Color("coral"))
        return fps_text        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                #self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = False
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = False
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = False

    def reset_keys(self):
        (
            self.UP_KEY,
            self.DOWN_KEY,
            self.BACK_KEY,
            self.START_KEY,
            self.LEFT_KEY,
            self.RIGHT_KEY,
        ) = (False, False, False, False, False, False)


    def game_loop(self):
        ## TO DO - create decorator that will do that - we are always using this one
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False

            pygame.display.update()


    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
