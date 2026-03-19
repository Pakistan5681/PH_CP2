from time import sleep
from pakistans_functions import *
from random import randint

class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.hunger = 100
        self.thirst = 100
        self.health = 100
        self.happiness = 100
        self.energy = 100
        self.awake = True
        self.alive = True
        self.skill = 5
        
    def normalize_vars(self):
        if self.hunger > 100: self.hunger = 100
        if self.thirst > 100: self.thirst = 100
        if self.happiness > 100: self.happiness = 100
        if self.energy > 100: self.energy = 100
        if self.health > 100: self.health = 100
        if self.hunger < 0: self.hunger = 0
        if self.thirst < 0: self.thirst = 0
        if self.happiness < 0: self.happiness = 0
        if self.energy < 0: self.energy = 0
        if self.health < 0: self.health = 0
        
    def day_stat_change(self):
        self.hunger -= 20
        self.thirst -= 20
        self.happiness -= 20

        if self.hunger < 20: 
            self.health -= 10
            self.happiness -= 75
        if self.thirst < 20: 
            self.health -= 10
            self.happiness -= 75
        if self.happiness < 20: self.health -= 5

        if self.hunger > 95: self.happiness += 10
        if self.thirst > 95: self.happiness += 10

        if self.health <= 0:
            self.alive = False

        if self.energy <= 0:
            self.send_to_bed()

        if not self.awake:
            self.awake = True

        self.normalize_vars()

    def feed(self, food_type):
        match food_type:
            case "Basic Food":
                self.hunger += 50
            case "Super Food":
                self.hunger = 100
                self.energy += 15
            case "Wet Food":
                self.hunger += 50
                self.thirst += 50
            case "Medicinal Food":
                self.hunger += 50
                self.health += 15
            case "Tasty Food":
                self.hunger += 50
                self.happiness += 15

        print_cool(f"Fed {self.name} {food_type} feed")
        self.normalize_vars()

    def water(self):
        self.thirst += 50
        if self.thirst > 100: self.thirst = 100
        print_cool(f"{self.name} drank much water (maybe a little too much if you ask me)")

    def send_to_bed(self):
        self.awake = False
        self.energy = 100
        print_cool(f"{self.name} is now asleep")

    def play(self):
        self.happiness += 50
        self.hunger -= 5
        self.thirst -= 5
        self.energy -= 25
        self.normalize_vars()
        print_cool(f"{self.name} had fun playing (i think)")

    def print_status(self):
        def get_bar(amount, name):
            out = f"{name} " 
            for i in range(10):
                if amount > i * 10:
                    out += "█"
                else:
                    out += "░"

            out += " "
            out += f"({amount}%)"

            print_cool(out, 0.025)

        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"skill: {self.skill}")
        get_bar(self.hunger, "hunger")
        get_bar(self.thirst, "thirst")
        get_bar(self.energy, "energy")
        get_bar(self.health, "health")
        get_bar(self.happiness, "happiness")
        
    def basic_print(self):
        if self.alive:
            if self.awake:
                return f"{self.name}, Age {self.age}"
            else:
                return f"{self.name} is sleeping."
        else:
            return f"{self.name} died at age {self.age}"
        
    def interaction_options(self, inventory):
        options = ["1", "2", "3", "4", '5', '6']
        while True:
            print(" ")
            print_cool("1. Feed", 0.01)
            print_cool("2. Water", 0.01)
            print_cool("3. Play", 0.01)
            print_cool("4. Send to Bed", 0.01)
            print_cool("5. Display Status", 0.01)
            print_cool("6. Exit", 0.01)
            option = idiot_proof_specific("Select the number of desired option ", options, "Either you already did that or that isn't a valid option")
            match option:
                case '1':
                    self.feed("Basic Food")
                    options.remove('1')
                case '2':
                    self.water()
                    options.remove('2')
                case '3':
                    self.play()
                    options.remove('3')
                case '4':
                    self.send_to_bed()
                    break
                case '5':
                    self.print_status()
                case '6':
                    break

class Inv_Item:
    def __init__(self, name, amount, type, shop_price):
        self.name = name
        self.amount = amount
        self.type = type
        self.shop_price = shop_price

shop = [
    Inv_Item("Basic Food", 1, "feed", 5),
    Inv_Item("Super Food", 1, "feed", 10),
    Inv_Item("Wet Food", 1, "feed", 7),
    Inv_Item("Medicinal Food", 1, "feed", 12),
    Inv_Item("Tasty Food", 1, "feed", 8),
    Inv_Item("Infinite Basic Food", 1, "feed", 500),
    Inv_Item("Infinite Super Food", 1, "feed", 1500),
    Inv_Item("Infinite Wet Food", 1, "feed", 750),
    Inv_Item("Infinite Medicinal Food", 1, "feed", 2000),
    Inv_Item("Infinite Tasty Food", 1, "feed", 1250),
    Inv_Item("Auto-feeder", 1, "automation", 300),
    Inv_Item("Advanced Auto-feeder", 1, "automation", 750),
    Inv_Item("Auto-water", 1, "automation", 250)
]
                
pets = []
inventory = [Inv_Item("Basic Food", 5, "feed", 5)]
money = 0

def menu(pets, money):
    if bool(pets):
        pets, money = day(pets)
    else:
        pets = fast_start()
        day(pets)

    return pets, money

def day(pets):
    if idiot_proof_yes_no("Would you like to buy something? "):


    for i in pets: i.day_stat_change()
    while True:
        validPets = []
        print(" ")
        for i in pets: 
            print_cool(i.basic_print())
            if i.alive and i.awake:
                validPets.append(i)

        if not bool(validPets): break

        currentPet = 0
        while True:
            pet = idiot_proof_specific("What pet would you like to interact with? ", get_pet_names(pets))
            print(" ")
            if pets[get_pet_index(pet, pets)].awake and pets[get_pet_index(pet, pets)].alive:
                currentPet = get_pet_index(pet, pets)
                break
            else:
                if not pets[get_pet_index(pet, pets)].alive: print_cool("That pet is dead")
                elif not pets[get_pet_index(pet, pets)].awake: print_cool("That pet is sleeping")

        pets[currentPet].print_status()
        pets[currentPet].interaction_options([])

        if not idiot_proof_yes_no("Would you like to interact with another pet? "):
            break

    print_cool("Your pigs are working")
    money = getMone(pets)
    return pets, money
    
def getAmount(chance):
    if chance >= 100:
        return 50
    elif chance >= 75:
        return 25
    elif chance >= 50:
        return 13
    elif chance >= 25:
        return 7
    elif chance >= 10:
        return 3
    else:
        return 1


def getMone(pets):
    total = 0
    for i in pets:
        if i.awake and i.alive:
            chance = i.skill + randint(0, 100)
            total += getAmount(chance)

    print_cool(f"You earned ${total} today")
    return total    

def get_pet_names(pets):
    out = []
    for i in pets:
        out.append(i.name)

    return out

def get_pet_index(name, pets):
    for i in pets:
        if i.name == name:
            return pets.index(i)    

def new_pet():
    print_cool("You got a new pig!")
    sleep(0.5)
    name = input_cool("What would you like to name your pig? ")
    print_cool(f"You now have a new pig named {name}!")
    return Pet(name)

def start():
    print_cool("Welcome to Pakistans Slave Labor Simulator!")
    sleep(1)
    print_cool("I mean, welcome to Pakistans Pig Farm Simulator!")
    sleep(0.5)
    print_cool("Of course")
    sleep(0.5)
    print_cool("...", 0.5)
    sleep(1)
    print_cool("Anyway, lets get you started")
    print_cool("I'm giving you this stater pig for free, but don't expect any more charity outta me")
    print_cool("You know, like, inflation, or something")
    print_cool("Make sure it doesn't die, and don't overwork it")
    print_cool("Good luck, I guess")
    sleep(2)
    return [new_pet()]

def fast_start():
    return [Pet("Jorp")]


while True:
    pets, money = menu(pets, money)