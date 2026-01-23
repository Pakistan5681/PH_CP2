import Render_Base as rb
import pygame as py
import numpy as np

py.init()
screen = py.display.set_mode((1280 * 1.5, 720 * 1.5))
clock = py.time.Clock()
running = True

fov = np.radians(60)
aspect = 16/9
near, far = 0.1, 100
f = 1 / np.tan(fov / 2)

pMatrix = np.array([
    [f/aspect, 0, 0, 0],
    [0, f, 0, 0],
    [0, 0, (far+near)/(near-far), (2*far*near)/(near-far)],
    [0, 0, -1, 0]
])

playerpos = rb.Vertex(0, 0, 0)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange  = (255, 102, 0)
purple = (255, 0, 255)
grey = (125, 125, 125)

rect = rb.drawRect(pMatrix, screen, rb.Vertex(playerpos.x, playerpos.y, playerpos.z - 50), 5, 10, 7)
rect2 = rb.drawRect(pMatrix, screen, rb.Vertex(playerpos.x + 20, playerpos.y, playerpos.z - 50), 5, 10, 7)
rect3 = rb.drawRect(pMatrix, screen, rb.Vertex(playerpos.x - 20, playerpos.y, playerpos.z - 50), 5, 10, 7)

floor = rb.drawRect(pMatrix, screen, rb.Vertex(0, -50, 50), 2, 50, 10)

while running:
    lastPlayerPos = rb.Vertex(playerpos.x, playerpos.y, playerpos.z)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False 

    keys = py.key.get_pressed()

    if keys[py.K_w]:
        playerpos.z -= 1
    elif keys[py.K_s]:
        playerpos.z += 1
    elif keys[py.K_a]:
        playerpos.x -= 1
    elif keys[py.K_d]:
        playerpos.x += 1

    amountToMove = rb.Vertex(-(playerpos.x - lastPlayerPos.x), -(playerpos.y - lastPlayerPos.y), -(playerpos.z - lastPlayerPos.z))

    screen.fill(red)

    rect.move(amountToMove)
    rect2.move(amountToMove)
    rect3.move(amountToMove)

    rect.draw(screen, pMatrix)
    rect2.draw(screen, pMatrix)
    rect3.draw(screen, pMatrix)   


    py.display.flip()
    clock.tick(60)

py.quit()
