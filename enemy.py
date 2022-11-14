import random
from config import *
import pygame

class Enemy:
    def __init__(self) -> None:
        self.position_X = (self.get_position() * DISPLAY_W)/9#int(width/2)
        self.position_Y = int(0 + DISPLAY_H/10)
        self.speed = 0.5
        self.change_Y = 0
        self.ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\Ship_10.png").convert()
        self.ship = pygame.transform.scale(self.ship, (1/12 * DISPLAY_W , 1/12 * DISPLAY_H))
        self.rect = self.ship.get_rect()

    def get_position(self):
        return(random.randint(3, 5)) 

    def move_X(self, change):
        self.change = change
        #print(self.position_X)

    def move_Y(self):
        self.change = 0.5 

    def draw(self, screen):
        self.change_Y = 0.1
        # self.position_X = 560
        # self.position_Y = int(DISPLAY_H - DISPLAY_H/10) - 30
        self.position_Y += self.change_Y
        screen.blit(self.ship, (self.position_X, self.position_Y))

    def get_coordinates(self):
        return (self.position_X, self.position_Y)