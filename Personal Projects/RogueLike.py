import pygame as py
from random import choice, randint

py.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (6, 69, 23)
BROWN = (82, 49, 2)
PLAYER_COLOR = (242, 177, 97)
SKY_BLUE = (2, 78, 122)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

running = True
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = py.time.Clock()
py.display.set_caption("Flesh Cube II")

playerX = SCREEN_WIDTH / 2
playerY = SCREEN_HEIGHT / 2
playerSpeed = 1

reloading = False
reloadClock = 0
reloadTime = 30

bullets = []
bulletSpeed = 3

regfoes = []
regSpawnClock = 0
regSpawnTime = 60
regFoeSpeed = 5

def get_foe_pos():
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
 
    out = []
 
    spawnOption = ["above", "below"] 
    option = choice(spawnOption)
 
    if option == "above":
        out.append(-150)
    else:
        out.append(SCREEN_WIDTH + 150)

    option = choice(spawnOption)

    if option == "above":
        out.append(-150)
    else:
        out.append(SCREEN_HEIGHT + 150)

    return out

while running:
    clock.tick(60)

    for event in py.event.get():
            if event.type == py.QUIT:
                running = False 

    keys = py.key.get_pressed()
    screen.fill(SKY_BLUE)

    if keys[py.K_a]:
        playerX -= playerSpeed
    if keys[py.K_d]:
        playerX += playerSpeed
    if keys[py.K_w]:
        playerY -= playerSpeed
    if keys[py.K_s]:
        playerY += playerSpeed

    player_pos = py.math.Vector2(playerX, playerY)
    mouse_pos = py.math.Vector2(py.mouse.get_pos())
    direction = mouse_pos - player_pos
    direction = direction.normalize() * bulletSpeed
    
    if keys[py.K_SPACE] and not reloading:
        bullets.append([playerX + 50, playerY + 50, direction.x, direction.y])
        reloading = True
        reloadClock = 0

    if reloading:
        reloadClock += 1
        if reloadClock >= reloadTime:
            reloading = False

    fullnew = []
    for i in bullets:
        new = [i[0] + i[2], i[1] + i[3], i[2], i[3]]
        py.draw.ellipse(screen, BLACK, (new[0], new[1], 20, 20))   
        fullnew.append(new)

    bullets = fullnew

    regSpawnClock += 1
    if regSpawnClock >= regSpawnTime:
        regfoes.append(get_foe_pos())
        regSpawnClock = 0

    fullnew = []
    for i in regfoes:
        new = i
        if playerX < i[0]:
            new[0] -= regFoeSpeed
        elif playerX > i[0]:
            new[0] += regFoeSpeed
        if playerY < i[1]:
            new[1] -= regFoeSpeed
        elif playerY > i[1]:
            new[1] += regFoeSpeed
        
        fullnew.append(new)

        py.draw.ellipse(screen, BLACK, (new[0], new[1], 50, 50))  

    regfoes = fullnew


    py.draw.ellipse(screen, WHITE, (playerX, playerY, 100, 100))
    if running: py.display.flip()