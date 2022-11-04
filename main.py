import pygame
from menu import *

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.playing = False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False
        self.DISPLAY_W = 480 * 2
        self.DISPLAY_H = 270 * 2
        self.DISPLAY_SIZE = (self.DISPLAY_W, self.DISPLAY_H)
        self.display = pygame.Surface(self.DISPLAY_SIZE)
        self.window = pygame.display.set_mode((self.DISPLAY_SIZE))
        self.font_name = ".\\fonts\\PixeloidMono-1G8ae.ttf"
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = MainMenu(self)
        self.volume_menu = VolumeMenu(self)
        self.music_volume = 0.3

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

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.BACK_KEY, self.START_KEY, self.LEFT_KEY, self.RIGHT_KEY = False, False, False, False, False, False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text("Thanks for playing", 20, self.DISPLAY_SIZE[0]/2, self.DISPLAY_SIZE[1]/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()


    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)



if __name__ == '__main__':
    g = Game()
    pygame.mixer.init()
    pygame.mixer.music.load('music/morgantj_-_I_m_Going_Bazurky.ogg')
    pygame.mixer.music.play()
    while g.running:
        g.curr_menu.display_menu()
        #g.playing = True
        g.game_loop()