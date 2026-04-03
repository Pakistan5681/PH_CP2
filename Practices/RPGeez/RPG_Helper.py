from Pakistans_Functions import pakistans_functions as pf
import faker as f
import matplotlib.pyplot as m
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
    
    def print_stats(self):
        print(self)
        print(" ")
        print(f"Strength: {self.str}, Dexterity: {self.dex}, Constitution: {self.const}")
        print(f"Intelligence: {self.int}, Wisdom: {self.wis}, Charisma: {self.char}")
        print(" ")
    
    def add_xp(self):
        if self.level:
            xp_cost = (2 ** (self.level - 1)) * 100

            xp_to_add = abs(pf.idiot_proof_general("How much xp do you want to add? "))
            self.xp += xp_to_add

            if self.xp >= xp_cost:
                while self.xp >= xp_cost and self.level:
                    self.xp -= xp_cost
                    xp_cost = (2 ** (self.level - 1)) * 100
                    self.level_up()
            else:
                print(f"Added {xp_to_add} xp! ({self.xp} / {xp_cost})")
                print(" ")
        else:
            print(f"{self.name} is already max level")

    def level_up(self):
        self.level += 1
        print(f"{pf.YELLOWTEXT}{self.name} levelled up to level {pf.UNDERLINE}{self.level}{pf.RESET}")
        print("1. Strength")
        print("2. Dexterity")
        print("3. Constitution")
        print("4. Intelligence")
        print("5. Wisdom")
        print("6. Charisma")
        print(" ")
        option = pf.idiot_proof_num_range("Enter the numbered option of the stat you want to increase ", 1, 6)
        print(" ")
        self.print_stats()
        print(" ")

        match option:
            case 1: self.str += 1 
            case 2: self.dex += 1 
            case 3: self.const += 1 
            case 4: self.int += 1 
            case 5: self.wis += 1 
            case 6: self.char += 1 

    def display_stat_chart(self):
        stats = [self.str, self.dex, self.const, self.int, self.wis, self.char]
        labels = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        m.pie(stats, labels=labels)
        m.title(f"{self.name}'s Stats (Lvl. {self.level})")
        m.show()

class Inv_Item():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

def main():
    characters = load()
    print(" ")

    while True:      
        print("1. Create Character")
        print("2. Create Random Character")
        print("3. Manage Character")
        print("4. Display Characters")
        print("5. Visualize Character Stats")
        print("6. Character Comparison")
        option = pf.idiot_proof_num_range("Select option ", 1, 6)

        match option:
            case 1: characters.append(create_character())
            case 2: characters.append(create_random())
            case 3: manage_character(characters)
            case 4: display_all(characters)
            case 5: display_stats_visual(characters)
            case 6: character_comparison(characters)

        save(characters)

def manage_character(characters):
    starting_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]

    print(" ")
    charNameRef = {}
    for i in characters: 
        charNameRef[i.name] = i
        print(i)
    print(" ")
    character = charNameRef[pf.idiot_proof_specific("What character do you want to change? ", list(charNameRef.keys()))]

    print("1. Add xp")
    print("2. Change weapon")
    print("3. Change name")
    option = pf.idiot_proof_num_range("Select numbered option: ", 1, 3)
    print(" ")

    match option:
        case 1: character.add_xp()
        case 2:
            print(f"{starting_weapons[0]}, {starting_weapons[1]}, {starting_weapons[2]}")
            print(f"{starting_weapons[3]}, {starting_weapons[4]}, {starting_weapons[5]}")
            print(f"{starting_weapons[6]}, {starting_weapons[7]}, {starting_weapons[8]}")
            print(f"{starting_weapons[9]}, {starting_weapons[10]}, {starting_weapons[11]}")
            print(f"{starting_weapons[12]}, {starting_weapons[13]}")

            weapon = pf.idiot_proof_specific("Which of these weapons do you want to change to? ", starting_weapons)
            character.weapon = weapon
        case 3:
            name = input("What name do you want to give your character? ")
            character.name = name


def create_character():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
    starting_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]

    name = input("What would you like to name your character? ")
    race = pf.idiot_proof_specific("what race is your character? ", races)
    classType = pf.idiot_proof_specific("what class is your character? ", classes)

    print(" ")
    print(f"{starting_weapons[0]}, {starting_weapons[1]}, {starting_weapons[2]}")
    print(f"{starting_weapons[3]}, {starting_weapons[4]}, {starting_weapons[5]}")
    print(f"{starting_weapons[6]}, {starting_weapons[7]}, {starting_weapons[8]}")
    print(f"{starting_weapons[9]}, {starting_weapons[10]}, {starting_weapons[11]}")
    print(f"{starting_weapons[12]}, {starting_weapons[13]}")
    print(" ")

    weapon = pf.idiot_proof_specific("Which of these weapons do you want to start with? ", starting_weapons)

    new = Character(name, race, classType, weapon)
    new.str = randint(5, 15)
    new.dex = randint(5, 15)
    new.const = randint(5, 15)
    new.int = randint(5, 15)
    new.wis = randint(5, 15)
    new.char = randint(5, 15)

    return new

def create_random():
    print(" ")
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
    starting_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
    fake = f.Faker()
    name = fake.first_name()
    race = choice(races)
    clasS = choice(classes)
    weap = choice(starting_weapons)
    new = Character(name, race, clasS, weap)

    new.str = randint(5, 15)
    new.dex = randint(5, 15)
    new.const = randint(5, 15)
    new.int = randint(5, 15)
    new.wis = randint(5, 15)
    new.char = randint(5, 15)

    print(f"Created {new}")
    print(" ")
    return new

def display_stats_visual(characters):

    print(" ")
    charNameRef = {}
    for i in characters: 
        charNameRef[i.name] = i
        print(i)
    print(" ")
    character = charNameRef[pf.idiot_proof_specific("What character do you want to change? ", list(charNameRef.keys()))]

    character.display_stat_chart()

    

def characters_to_df(chars):
    data = []
    for c in chars:
        data.append({
            "name": c.name,
            "race": c.race,
            "class": c.classType,
            "level": c.level,
            "xp": c.xp,
            "strength": c.str,
            "dexterity": c.dex,
            "constitution": c.const,
            "intelligence": c.int,
            "wisdom": c.wis,
            "charisma": c.char,
            "weapon": c.weapon
        })
    return p.DataFrame(data)

def character_comparison(chars):
    while True:
        df = characters_to_df(chars)
        print(" ")
        print("1. Print Data")
        print("2. Print Nerd Data")
        print("3. Get Highest")
        print("4. Get Stat Averages")
        print("5. Visualize All Data")
        print("6. Quit")
        print(" ")
        option = pf.idiot_proof_num_range("Type the numbered option ", 1, 6)
        print(" ")

        match option:
            case 1:
                print(df)
            case 2:
                print(df.describe())
            case 3:
                print("1. Level")
                print("2. Strength")
                print("3. Dexterity")
                print("4. Constitution")
                print("5. Intelligence")
                print("6. Wisdom")
                print("7. Charisma")
                print(" ")
                option2 = pf.idiot_proof_num_range("Type the numbered option ", 1, 7)
                print(" ")

                stat = ""
                match option2:
                    case 1: stat = "level"
                    case 2: stat = "strength"
                    case 3: stat = "dexterity"
                    case 4: stat = "constitution"
                    case 5: stat = "intelligence"
                    case 6: stat = "wisdom"
                    case 7: stat = "charisma" 

                idx = df[stat].idxmax()
                row = df.loc[idx]
                print(f"{row["name"]}: {stat.capitalize()} {row[stat]}") 
            case 4:
                avg_stats = df[[
                    "strength", "dexterity", "constitution",
                    "intelligence", "wisdom", "charisma"
                ]].mean() 

                stats = [avg_stats["strength"], avg_stats["dexterity"], avg_stats["constitution"], avg_stats["intelligence"], avg_stats["wisdom"], avg_stats["charisma"]]
                labels = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

                avg_stats.index = [s.capitalize() for s in avg_stats.index]
                avg_stats.plot(kind="bar")

                m.title("Average Stats")
                m.show()
            case 5:
                stats_df = df[[
                    "name",
                    "strength", "dexterity", "constitution",
                    "intelligence", "wisdom", "charisma"
                ]]

                stats_df = stats_df.set_index("name")

                stats_df.plot(kind="bar")

                m.title("All Character Stats")
                m.ylabel("Stat Value")
                m.xticks(rotation=45)
                m.tight_layout()
                m.show()
            case 6: break


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
            json.dump(saveChars, file, indent=4)

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