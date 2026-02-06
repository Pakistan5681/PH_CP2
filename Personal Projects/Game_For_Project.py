import pygame as py
from random import randint

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

hazards = [] # position (on the x axis) of every hazard

ground = (SCREEN_HEIGHT / 12) * 9 # The lowest point the player can be

fps = 60
max_fps = 500

score = 0

font = py.font.Font(None, 36)

spike_colliders = []

PLAYER_X = SCREEN_WIDTH / 8 
playerY = ground 

PLAYER_WIDTH = SCREEN_WIDTH / 17
PLAYER_HEIGHT = SCREEN_HEIGHT / 5

SPIKE_WIDTH = 75
SPIKE_HEIGHT = 75

moveSpeed = 5

yVel = 0
gravity = 0.5

touchingGround = True

spawnTimer = 0
spawnEveryXFrames = 90

while running:
    screen.fill(SKY_BLUE)

    clock.tick(fps)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 

    keys = py.key.get_pressed()

    if keys[py.K_SPACE]: 
        if touchingGround:
            yVel = -20
            touchingGround = False

    if not touchingGround: yVel += gravity
    playerY += yVel
    
    if playerY >= ground and not touchingGround:
        touchingGround = True
        playerY = ground
        yVel = 0

    print(f"{fps}")

    player_rect = py.Rect(
        PLAYER_X,
        playerY - PLAYER_HEIGHT,
        PLAYER_WIDTH,
        PLAYER_HEIGHT
    )

    py.draw.rect(screen, BROWN, (0, ground, SCREEN_WIDTH, ground)); py.draw.rect(screen, GREEN, (0, ground, SCREEN_WIDTH, ground / 15))
    py.draw.rect(screen, PLAYER_COLOR, player_rect)

    spawnTimer += 1

    if spawnTimer == spawnEveryXFrames:
        hazards.append(SCREEN_WIDTH + SPIKE_WIDTH)
        spawnTimer = 0
        spawnEveryXFrames = randint(90, 240)

        spike_colliders.append(py.Rect(
            SCREEN_WIDTH,
            ground - SPIKE_HEIGHT,
            SPIKE_WIDTH,
            SPIKE_HEIGHT
        ))

    text_surface = font.render('Hello World!', True, BLACK)
    screen.blit(text_surface, (100, 100, 100, 100))


    for i in spike_colliders:
        if player_rect.colliderect(i):
            running = False

    for i in range(len(hazards)):
        hazards[i] -= moveSpeed

        spike_rect = py.Rect(
            hazards[i] - SPIKE_WIDTH,
            ground - SPIKE_HEIGHT,
            SPIKE_WIDTH,
            SPIKE_HEIGHT
        )

        py.draw.rect(screen, RED, spike_rect)

        if player_rect.colliderect(spike_rect):
            running = False        

        if hazards[i] < PLAYER_X

    if fps < max_fps: fps += 0.05

    py.display.flip()

