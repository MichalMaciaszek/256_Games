import pygame
import time
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    KEYUP,
)


size = width, height = (1024, 1024)


pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

icon = pygame.image.load("D:\\Python_projects\\256 Games\\images\\Ship.png")
pygame.display.set_icon(icon)

# screen.fill((255, 255, 255))
# pygame.display.update()


player_ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\Ship_10.png")
#player_ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\spaceship-png-icon-19.png")
playerX = width/2
playerY = int(height - height/10)


enemy_ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\Ship_10.png")
#player_ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\spaceship-png-icon-19.png")
enemyX = width/2
enemyY = int(0 + height/10)


change_X = 0
change_Y = 0

speed = 0.1

class Player:
    def __init__(self) -> None:
        self.position_X = int(width/2)
        self.position_Y = int(height - height/10)
        self.speed = 0.5
        self.change = 0
        self.ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\Ship_10.png")

    def move_X(self, change):
        self.change = change 
        print(self.position_X)

    def move_Y(self, change):
        pass

    def draw(self):
        self.position_X += self.change
        screen.blit(self.ship, (self.position_X, self.position_Y))

    def get_coordinates(self):
        return (self.position_X, self.position_Y)


# DESIGN SECTION
######### (let those be total field)
   ###    (and we want those, cause rest would be a backround in this mode)
   #      (this starts at 3 * width/9)
     #    (this is 5 * width/9)

def get_position():
    return(random.randint(3, 5)) 

class Enemy:
    def __init__(self) -> None:
        self.name = random.randbytes(3)
        print(self.name)
        self.position_X = (get_position() * width)/9#int(width/2)
        self.position_Y = int(0 + height/10)
        self.speed = 0.5
        self.change_Y = 0
        self.ship = pygame.image.load("D:\\Python_projects\\256 Games\\images\\Ship_10.png")

    def move_X(self, change):
        self.change = change
        #print(self.position_X)

    def move_Y(self):
        self.change = 0.5 

    def draw(self):
        self.change_Y = 0.1
        self.position_Y += self.change_Y
        screen.blit(self.ship, (self.position_X, self.position_Y))

    def get_coordinates(self):
        return (self.position_X, self.position_Y)

import math
def isCollision(a_cordinates, b_cordinates):
    print(a_cordinates)
    print(b_cordinates)
    distance = (math.sqrt(math.pow(a_cordinates[0] - b_cordinates[0], 2)) + (math.pow(a_cordinates[1] - b_cordinates[1], 2)))
    print(distance)
    if distance < 25:
        return True
    return False


enemies = list()
enemyA = Enemy()
enemies.append(enemyA)
print(enemies)

start = pygame.time.get_ticks()

player = Player()

while running:

    screen.fill((255, 255, 255))

    now = pygame.time.get_ticks()
    if now - start > 2000:
        start = now
       # enemy = Enemy(60, 200, player)
        enemies.append(Enemy())

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_X(-(player.speed)) #= -(player.speed) #change_X = -(speed)

            if event.key == K_RIGHT:
                player.move_X(player.speed)
                #change_X = speed

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.move_X(0)

            if event.key == K_ESCAPE:
                running = False



    # if isCollision(playerX, playerY, enemyX, enemyY):
    #     print("Colission")
    #     enemies.remove("a")


    # if playerX <= 0:
    #     playerX = 0
    # elif playerX >= width - width/10:
    #     playerX = width - width/10

        if event.type == QUIT:
            running = False
    
    # enemyY += 0.1
    # playerX += change_X
    player.draw()#playerX, playerY)

    for e in enemies:
        e.draw()    
        if isCollision(e.get_coordinates(), player.get_coordinates()):
            print("colision")
            enemies.remove(e)
    #     enemy(enemyX, enemyY)
    #     if isCollision(playerX, playerY, enemyX, enemyY):
    #         print("Colission")
    #         enemies.remove(e)



    pygame.display.update()


pygame.quit()