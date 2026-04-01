from Pakistans_Functions import pakistans_functions as pf
import faker as f
import matplotlib as m
import pandas as p
from random import choice, randint
import os
import json

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
    
    def add_xp(self):
        xp_cost = (2 ^ (self.level - 1)) * 100

        while self.xp > xp_cost:
            self.xp -= xp_cost
            self.level_up()

    def level_up(self):
        print("1. Strength")
        print("2. Dexterity")
        print("3. Constitution")
        print("4. Intelligence")
        print("5. Wisdom")
        print("6. Charisma")
        option = pf.idiot_proof_num_range(f"{self.name} leveled up! Enter the numbered option of the stat you want to increase ")

        match option:
            case 1:

class Inv_Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

def main():
    characters = load()
    while True:
        print("1. Create Character")
        print("2. Create Random Character")
        print("3. Manage Character")
        print("4. Display Characters")
        option = pf.idiot_proof_num_range("Select option ", 1, 4)

        match option:
            case 1: characters.append(create_character())
            case 2: characters.append(create_random())
            case 3: pass
            case 4: display_all(characters)

        save(characters)

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
    print(" ")
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
    starting_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
    fake = f.Faker()
    name = fake.name()
    race = choice(races)
    clasS = choice(classes)
    weap = choice(starting_weapons)

    print(f"Created {Character(name, race, clasS, weap)}")
    print(" ")
    return Character(name, race, clasS, weap)

def display_all(chars):
    print(" ")
    for i in chars:
        print(i)
    print(" ")

def save(chars):
    if os.path.isfile("Practices/RPGeez/char_saves.json"):
        with open("Practices/RPGeez/char_saves.json", "w") as file:
            saveChars = []
            for i in chars:
                saveChars.append(i.__dict__)
            json.dump(saveChars, file)

def load():
    if os.path.isfile("Practices/RPGeez/char_saves.json"):
            try:
                with open("Practices/RPGeez/char_saves.json", "r") as file:
                    jsonData = json.load(file)
                    chars = []
                    for i in jsonData:
                        newChar = Character(i["name"], i["race"], i["classType"], i["weapon"])
                        newChar.level = i["level"]
                        newChar.inventory = i["inventory"]
                        newChar.str = i["str"]
                        newChar.dex = i["dex"]
                        newChar.int = i["int"]
                        newChar.const = i["const"]
                        newChar.wis = i["wis"]
                        newChar.char = i["char"]
                        newChar.xp = i["xp"]

                        chars.append(newChar)

                    return chars
            except json.JSONDecodeError:
                return []

main()