import pygame
from menu import *
import math
from config import DISPLAY_W, DISPLAY_H
from player import Player
from enemy import Enemy
from colissions import isCollision


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.Boundaries_L_R_U_D = [1.5 / 6, 4.5 / 6, 0, 0]

        self.running = True
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
        self.font_name = ".\\fonts\\PixeloidMono-1G8ae.ttf"
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = MainMenu(self)
        self.volume_menu = VolumeMenu(self)
        self.music_volume = 0.1
        self.font = pygame.font.Font(self.font_name, 10)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
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

    def update_fps(self, now, font):
        fps = str(int(now.get_fps()))
        fps_text = font.render(fps, 60, pygame.Color("red"))
        return fps_text

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
                (0, 0, self.DISPLAY_W *
                 (self.Boundaries_L_R_U_D[0]), self.DISPLAY_H),
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
            player.rect = player.ship.get_rect(
                topleft=(player.position_X, player.position_Y)
            )
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
                    self.draw_text(
                        "Colission", 60, self.DISPLAY_W, self.DISPLAY_H / 2 - 20
                    )
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

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)


if __name__ == "__main__":
    g = Game()
    pygame.mixer.init()
    pygame.mixer.music.load("music/morgantj_-_I_m_Going_Bazurky.ogg")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(g.music_volume)

    while g.running:
        g.curr_menu.display_menu()
        # g.playing = True
        g.game_loop()
