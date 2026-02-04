import pygame as py

py.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (155, 118, 83)
SKY_BLUE = (135, 206, 235)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = py.time.Clock()
py.display.set_caption("Runner")

hazards = [] # position (on the x axis) of every hazard

ground = (SCREEN_HEIGHT / 3) * 2 # The lowest point the player can be

fps = 30

PLAYER_X = SCREEN_WIDTH / 4 
playerY = ground 

while True:
    screen.fill(SKY_BLUE)

    py.draw.rect(screen, BROWN, )

