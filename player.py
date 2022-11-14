from config import *
import pygame

# IMAGE_SMALL = pg.transform.scale(IMAGE, (50, 30))


class Player:
    def __init__(self) -> None:
        self.position_X = int(DISPLAY_W / 2)
        self.position_Y = int(DISPLAY_H - DISPLAY_H / 10)
        self.speed = 0.3
        self.change = 0
        self.ship = pygame.image.load(
            "D:\\Python_projects\\256 Games\\images\\Ship_10.png"
        ).convert()
        self.ship = pygame.transform.scale(
            self.ship, (1 / 12 * DISPLAY_W, 1 / 12 * DISPLAY_H)
        )
        self.ship_width = self.ship.get_width()
        self.rect = self.ship.get_rect()

    def movement(self, game):
        if game.LEFT_KEY:
            if self.position_X >= game.Boundaries_L_R_U_D[0] * DISPLAY_W:
                self.move_X(-(self.speed))
            else:
                self.move_X(0)
        elif game.RIGHT_KEY:
            if (
                self.position_X
                < game.Boundaries_L_R_U_D[1] * DISPLAY_W - self.ship_width
            ):
                self.move_X(self.speed)
            else:
                self.move_X(0)
        else:
            self.move_X(0)

    def move_X(self, change):
        self.change = change

    def move_Y(self, change):
        pass

    def draw(self, screen):
        self.position_X += self.change
        screen.blit(self.ship, (self.position_X, self.position_Y))

    def get_coordinates(self):
        return (self.position_X, self.position_Y)
