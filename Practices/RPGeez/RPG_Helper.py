from Pakistans_Functions import pakistans_functions as pf
import faker as f
import matplotlib as m
import pandas as p
from random import choice, randint

class Character():
    def __init__(self, name, race, classType, weapon):
        self.name = name
        self.race = race
        self.classType = classType
        self.level = 1
        self.inventory = []
        self.weapon = weapon
        self.str = 10
        self.dex = 10
        self.int = 10
        self.const = 10
        self.wis = 10
        self.char = 10
        self.xp = 0

    def __str__(self):
        return f"{self.name} ({self.race} {self.classType}), level {self.level}."

class Inv_Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

def main():
    while True:
        print("1. Create Character")
        print("2. Create Random Character")
        print("3. Manage Character")
        option = pf.idiot_proof_num_range("Select option", 1, 3)

        match option:
            case 1: create_character()
            case 2: create_random()

def create_character():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
    starting_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]

    name = input("What would you like to name your character? ")
    race = pf.idiot_proof_specific("what race is your character? ", races)
    classType = pf.idiot_proof_specific("what class is your character? ", classes)

    print(f"{starting_weapons[0]}, {starting_weapons[1]}, {starting_weapons[2]}")
    print(f"{starting_weapons[3]}, {starting_weapons[4]}, {starting_weapons[5]}")
    print(f"{starting_weapons[6]}, {starting_weapons[7]}, {starting_weapons[8]}")
    print(f"{starting_weapons[9]}, {starting_weapons[10]}, {starting_weapons[11]}")
    print(f"{starting_weapons[12]}, {starting_weapons[13]}")

    weapon = pf.idiot_proof_specific("Which of these weapons do you want to start with? ", starting_weapons)
    return Character(name, race, classType, weapon)

def create_random():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
    starting_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
    fake = f.Faker()
    name = fake.name()
    race = choice(races)
    clasS = choice(classes)
    weap = choice(starting_weapons)

    return Character(name, race, clasS, weap)

main()