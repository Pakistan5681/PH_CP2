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

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange  = (255, 102, 0)
purple = (255, 0, 255)

rect = rb.drawRect(pMatrix, screen, rb.Vertex(0, 0, -50), 5, 10, 7)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill(purple)
    

    rect.rotate("y", rb.Vertex(0, 0, -50), 1)
    rect.draw(screen, pMatrix)

    py.display.flip()
    clock.tick(60)

py.quit()
