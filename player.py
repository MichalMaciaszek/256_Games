from config import *
import pygame
from pathlib import Path
image_folder = Path("images")

class Player:
    def __init__(self, starting_position_relative: tuple() = None) -> None:
        
        self.ship = pygame.image.load(image_folder / "Ship_10.png").convert()
        transColor = pygame.Color(255, 255, 255)
        self.ship.set_colorkey(transColor)#.convert_alpha()
        self.ship = pygame.transform.scale(self.ship, (1 / 12 * DISPLAY_W, 1 / 12 * DISPLAY_H))
        self.ship_width = self.ship.get_width()
        self.ship_height = self.ship.get_height()
        self.rect = self.ship.get_rect()
        
        if starting_position_relative is None:
            self.position_X = int(DISPLAY_W / 2 - self.ship_width/2)
            self.position_Y = int(DISPLAY_H - DISPLAY_H / 10)
        else:
            self.position_X  = int(DISPLAY_W / starting_position_relative[0] - self.ship_width/2)
            self.position_Y  = int(DISPLAY_H / starting_position_relative[1])
            
            
        self.speed = DISPLAY_H / 500
        self.max_speed = DISPLAY_H / 500
        self.change = 0
        self.change_Y = 0
        self.change_X = 0
        self.current_force = 0


    def rotate_to_side(self):
        pass

    def movement_X(self, game):
        if game.LEFT_KEY:
            if self.position_X >= game.Boundaries_L_R_U_D[0] * DISPLAY_W:
                self.set_X_change(-(self.speed))
            else:
                self.set_X_change(0)
        elif game.RIGHT_KEY:
            if self.position_X < game.Boundaries_L_R_U_D[1] * DISPLAY_W - self.ship_width:
                self.set_X_change(self.speed)
            else:
                self.set_X_change(0)
        else:
            self.set_X_change(0)

    def movement_X_drift(self, game):
        if (self.position_X < game.Boundaries_L_R_U_D[0] * DISPLAY_W) or (self.position_X > game.Boundaries_L_R_U_D[1] * DISPLAY_W - self.ship_width):
            self.set_X_change(0)
            self.current_force = 0
        
        if game.LEFT_KEY:
            if self.position_X >= game.Boundaries_L_R_U_D[0] * DISPLAY_W:
                self.force_applied(-(self.speed/100))
            ### Leaving this else for now - it might be a little better otherway
            # else:
            #     self.current_force = 0
            #     self.set_X_change(0)
        elif game.RIGHT_KEY:
            if self.position_X < game.Boundaries_L_R_U_D[1] * DISPLAY_W - self.ship_width:
                self.force_applied((self.speed/100))
            # else:
            #     self.current_force = 0
            #     self.set_X_change(0)
        
        else:
            self.force_applied(0)
            



    def movement_Y(self, game):
        if game.UP_KEY:
            if self.position_Y >= game.Boundaries_L_R_U_D[3] * DISPLAY_H:
                self.set_Y_change(-(self.speed))
            else:
                self.set_Y_change(0)
        elif game.DOWN_KEY:
            if self.position_Y < game.Boundaries_L_R_U_D[2] * DISPLAY_H - self.ship_height:
                self.set_Y_change(self.speed)
            else:
                self.set_Y_change(0)
        else:
            self.set_Y_change(0)    

    def set_X_change(self, change):
        self.change_X = change
    
    #this is more intuitive
    def force_applied(self, force):
                
        if force == 0 and self.current_force > 0:
            self.current_force -= 0.01
            if self.current_force < 0:
                self.current_force = 0
        
        elif force == 0 and self.current_force < 0:
            self.current_force += 0.01
            if self.current_force > 0:
                self.current_force = 0
            
        elif force > 0 and self.current_force < 0:
            self.current_force = 0
            
        elif force < 0 and self.current_force > 0:
            self.current_force = 0
            
        elif abs(self.current_force) <= self.max_speed:
            self.current_force += force
        
        self.set_X_change(self.current_force)

    def set_Y_change(self, change):
        self.change_Y = change

    def draw(self, screen):
        self.position_X += self.change_X
        self.position_Y += self.change_Y
        screen.blit(self.ship, (self.position_X, self.position_Y))

    def get_coordinates(self):
        return (self.position_X, self.position_Y)
