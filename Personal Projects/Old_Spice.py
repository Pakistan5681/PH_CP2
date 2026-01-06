import pygame as py

py.init

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BACKGROUND_COLOR = (0, 0, 255)

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Old Spice")

class Room:
    def __init__(self, name, doors, size, location, floor):
        self.name, self.doors, self.size, self.location, self.floor = name, doors, size, location, floor

    def Draw():
        

rooms = [Room("Front Room", ["Kitchen", "Living Room", "Downstairs Landing"], (3, 3), (0, 0), 1),
         Room("Living Room", ["Family Room", "Kitchen", "Upstairs Landing"]),
         Room("Kitchen", ["Garage", "Pantry", "Family Room", "Front Room"]),
         Room("Garage", ["Kitchen"]),
         Room("Pantry", ["Kitchen"]),
         Room("Upstairs Landing", ["Living Room", "Upstairs Bathroom", "Upstairs Bedroom", "Master Bedroom"]),
         Room("Master Bedroom", ["Upstairs Landing", "Master Bathroom"]),
         Room("Master Bathroom", ["Master Bedroom"]),
         Room("Upstairs Bathroom", ["Upstairs Landing"])
         ]