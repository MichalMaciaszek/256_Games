import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        #self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.level_choosex, self.level_choosey = self.mid_w, self.mid_h + 50
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.current_level = 1
        self.state_position = 0
        # "Start"
        self.options_map = ["Start", "Level", "Options", "Credits"]
        self.state = self.options_map[0]

        self.state_dict = {"Start": [self.startx, self.starty],
                           "Options": [self.optionsx, self.optionsy],
                           "Level": [self.level_choosex, self.level_choosey],
                           "Credits": [self.creditsx, self.creditsy],
                           }

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)

            self.game.draw_text(
                f"Level Choose: {self.current_level}", 20, self.level_choosex, self.level_choosey)
                
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def change_state(self, state, quantity):
        print(state)
        if state >= 1 and quantity < 0:
            state += quantity
        if state <= 2 and quantity > 0:
            state += quantity
        return state

    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.state_position = self.change_state(self.state_position, 1)
            self.state = self.options_map[self.state_position]
            self.cursor_rect.midtop = (
                self.state_dict[self.state][0] + self.offset, self.state_dict[self.state][1])

        if self.game.UP_KEY:
            self.state_position = self.change_state(self.state_position, -1)
            self.state = self.options_map[self.state_position]
            self.cursor_rect.midtop = (
                self.state_dict[self.state][0] + self.offset, self.state_dict[self.state][1])

        if self.game.LEFT_KEY:
            if self.state == "Level":
                self.current_level -= 1

        if self.game.RIGHT_KEY:
            if self.state == "Level":
                self.current_level += 1

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text(
                'Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (
                    self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

        elif self.game.START_KEY:
            # TO-DO: Create a Controls Menu
            self.game.curr_menu = self.game.volume_menu
            self.run_display = False

class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Set volume', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.volume_grid_size = [self.game.DISPLAY_W / 2 - self.game.music_volume * 60, self.game.music_volume * 60 * 2]
            pygame.draw.rect(self.game.display, self.game.WHITE, pygame.Rect((self.volume_grid_size[0], self.game.DISPLAY_H / 2), (self.volume_grid_size[1], 20)))

            self.blit_screen()

    def check_input(self):
        if self.game.START_KEY or self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.LEFT_KEY and self.game.music_volume >= 0:
                self.game.music_volume -= 0.1
                pygame.mixer.music.set_volume(self.game.music_volume)
        elif self.game.RIGHT_KEY and self.game.music_volume <= 1:
                self.game.music_volume += 0.1
                pygame.mixer.music.set_volume(self.game.music_volume)


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text(
                'Made by Michal Maciaszek', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text("Music:", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text("I'm Going Bazurky by morgantj (c) copyright 2011 Licensed under a Creative Commons Noncommercial Sampling Plus license.", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.game.draw_text("http://dig.ccmixter.org/files/morgantj/29944", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 90)

            self.blit_screen()
