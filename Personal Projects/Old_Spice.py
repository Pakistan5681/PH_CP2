"""
Room("Kitchen", ["Garage", "Pantry", "Family Room", "Front Room"], ),
         Room("Garage", ["Kitchen"]),
         Room("Pantry", ["Kitchen"]),
         Room("Upstairs Landing", ["Living Room", "Upstairs Bathroom", "Upstairs Bedroom", "Master Bedroom"]),
         Room("Master Bedroom", ["Upstairs Landing", "Master Bathroom"]),
         Room("Master Bathroom", ["Master Bedroom"]),
         Room("Upstairs Bathroom", ["Upstairs Landing"])
"""


import pygame as py
import pakistans_functions as pf

py.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 255)

RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Old Spice")

class Room:
    def __init__(self, name, doors, size, location, floor):
        self.name, self.doors, self.size, self.location, self.floor = name, doors, size, location, floor

    def Draw(self):
        py.draw.rect(screen, RED, (self.location[0], self.location[1], self.size[0], self.size[1]))
        

rooms = [Room("Front Room", ["Kitchen", "Living Room", "Downstairs Landing"], (50, 30), (275, 285), 1),
         Room("Living Room", ["Family Room", "Kitchen", "Upstairs Landing"], (50, 70), (325, 265), 1),
         ]

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill(BLACK)
    rooms[0].Draw()
    rooms[1].Draw()
    py.display.flip()
