from config import *
import pygame
from pathlib import Path
image_folder = Path("images")

class Heart:
    def __init__(self, number_of_lifes: int) -> None:
        self.lifes = number_of_lifes
        self.ship = pygame.image.load(image_folder / "heart.png").convert()
        self.ship = pygame.transform.scale(self.ship, (1 / 30 * DISPLAY_W, 1 / 30 * DISPLAY_H))
        
    def draw(self, screen):
        for life in range(self.lifes):
            screen.blit(self.ship, (((DISPLAY_W - DISPLAY_W/10) - life * 50), DISPLAY_H / 100))
