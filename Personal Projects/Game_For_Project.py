import pygame as py

py.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (155, 118, 83)
PLAYER_COLOR = (242, 177, 97)
SKY_BLUE = (135, 206, 235)

running = True

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = py.time.Clock()
py.display.set_caption("Flesh Cube II")

hazards = [55] # position (on the x axis) of every hazard

ground = (SCREEN_HEIGHT / 12) * 9 # The lowest point the player can be

fps = 30

PLAYER_X = SCREEN_WIDTH / 8 
playerY = ground 

PLAYER_WIDTH = SCREEN_WIDTH / 17
PLAYER_HEIGHT = SCREEN_HEIGHT / 5

SPIKE_WIDTH = 75
SPIKE_HEIGHT = 75

moveSpeed = 5

while running:
    screen.fill(SKY_BLUE)

    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 

    py.draw.rect(screen, BROWN, (0, ground, SCREEN_WIDTH, ground)); py.draw.rect(screen, GREEN, (0, ground, SCREEN_WIDTH, ground / 15))
    py.draw.rect(screen, PLAYER_COLOR, (PLAYER_X, playerY - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))

    for i in hazards:
        i -= moveSpeed
        py.draw.rect(screen, RED, (i - (SPIKE_WIDTH / 2), ground - SPIKE_HEIGHT, SPIKE_WIDTH, SPIKE_HEIGHT))

    py.display.flip()

