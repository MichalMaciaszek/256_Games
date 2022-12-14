import random
from config import *
import pygame
from pathlib import Path
image_folder = Path("images")
from enemies.enemy import Enemy

class Cars_Enemy(Enemy):
    def __init__(self) -> None:
        Enemy.__init__(self)
        self.position_X = (self.get_position() * DISPLAY_W) / 8.8  # int(width/2)
        self.position_Y = int(0 + DISPLAY_H / 10)
        self.speed =  DISPLAY_H / 700 
        self.change_Y = 0.1
        self.ship = pygame.image.load(image_folder / "Ship_10.png").convert()
        self.ship = pygame.transform.scale(self.ship, (1 / 12 * DISPLAY_W, 1 / 12 * DISPLAY_H))
        self.ship = pygame.transform.flip(self.ship, flip_x=False, flip_y=True)
        self.rect = self.ship.get_rect()

    def get_position(self):
        return random.randint(3, 5)

    def move_X(self, change):
        self.change = change

    def draw(self, screen):
        self.position_Y += self.speed
        screen.blit(self.ship, (self.position_X, self.position_Y))
