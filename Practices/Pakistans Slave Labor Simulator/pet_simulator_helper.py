from time import sleep
from pakistans_functions import *
from random import randint
import os
import json

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
        self.interacted = False
        
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
        self.interacted = False
        if self.awake: 
            self.health += 10
            self.hunger -= 10
            self.thirst -= 10
            self.happiness += 10
        else: 
            self.skill += randint(0,3)
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

        if self.hunger > 95: 
            self.happiness += 10
            self.health += 10
        if self.thirst > 95: 
            self.happiness += 10
            self.health += 10

        if self.health <= 0:
            self.alive = False

        if not self.awake:
            self.awake = True

        if self.energy <= 0:
            self.send_to_bed()

        self.normalize_vars()

    def autoFeed(self, foodType):
        match foodType:
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
        
        self.normalize_vars()

    def feed(self, inventory):
        # Food name : [inInventory, isInfinite]
        foods = {
            "Basic Food": [False, False],
            "Super Food": [False, False],
            "Wet Food": [False, False],
            "Medicinal Food": [False, False],
            "Tasty Food": [False, False],
        }

        foodTypes = ["Basic Food", "Super Food", "Wet Food", "Medicinal Food", "Tasty Food"]
        infinite = False

        for i in inventory:
            if i.name == "Basic Food": foods["Basic Food"] = [True, False]
            if i.name == "Infinite Basic Food": foods["Basic Food"] = [True, True]
            if i.name == "Super Food": foods["Super Food"] = [True, False]
            if i.name == "Infinite Super Food": foods["Super Food"] = [True, True]
            if i.name == "Wet Food": foods["Wet Food"] = [True, False]
            if i.name == "Infinite Wet Food": foods["Wet Food"] = [True, True]
            if i.name == "Medicinal Food": foods["Medicinal Food"] = [True, False]
            if i.name == "Infinite Medicinal Food": foods["Medicinal Food"] = [True, True]
            if i.name == "Tasty Food": foods["Tasty Food"] = [True, False]
            if i.name == "Infinite Tasty Food": foods["Tasty Food"] = [True, True]

        current = 1
        foodIndex = {}
        for i in inventory:
            if i.type == "feed":
                print(f"{current}. You have {i.name} (remaining: {i.amount})")
                foodIndex[str(current)] = i.name
                current += 1

        if not bool(list(foodIndex.keys())): 
            print("You have no food goober")
            return

        while True:
            print(" ")

            food_type = idiot_proof_specific(f"What food type do you want to feed {self.name}? Enter the number: ", list(foodIndex.keys()))     
            food_type = foodIndex[food_type]
            if foods[food_type][0]: 
                if foods[food_type][1]: infinite = True
                break
            else: print("You dont have that food ):")

        match food_type:
            case "Basic Food":
                self.hunger += 50
            case "Super Food":
                self.hunger = 100
                self.energy += 30
            case "Wet Food":
                self.hunger += 50
                self.thirst += 50
            case "Medicinal Food":
                self.hunger += 50
                self.health += 20
            case "Tasty Food":
                self.hunger += 50
                self.happiness += 30

        itemToRemove = ""
        for i in inventory:
            if i.name == food_type:
                if not foods[food_type][1]: itemToRemove = i
                break

        if not infinite: inventory = removeItemFromInventorY(inventory, itemToRemove)
        print(f"Fed {self.name} {food_type}")
        self.normalize_vars()

    def water(self):
        self.thirst += 50
        if self.thirst > 100: self.thirst = 100
        print(f"{self.name} drank much water (maybe a little too much if you ask me)")

    def send_to_bed(self):
        self.awake = False
        self.energy = 100
        print(f"{self.name} is now asleep")

    def play(self):
        self.happiness += 50
        self.hunger -= 5
        self.thirst -= 5
        self.energy -= 25
        self.normalize_vars()
        print(f"{self.name} had fun playing (i think)")

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

            print(out)

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
            print("1. Feed")
            print("2. Water")
            print("3. Play")
            print("4. Send to Bed")
            print("5. Display Status")
            print("6. Exit")
            option = idiot_proof_specific("Select the number of desired option ", options, "Either you already did that or that isn't a valid option")
            match option:
                case '1':
                    self.feed(inventory)
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
                    self.interacted = True
                    break

class Inv_Item:
    def __init__(self, name, amount, type, shop_price):
        self.name = name
        self.amount = amount
        self.type = type
        self.shop_price = shop_price

    def __str__(self):
        return f"{self.name}: ${self.shop_price}"

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
    Inv_Item("Auto-feeder", 1, "consumable", 300),
    Inv_Item("Advanced Auto-feeder", 1, "consumable", 750),
    Inv_Item("Auto-water", 1, "consumable", 250),
    Inv_Item("The Funinator", 1, "consumable", 425),
    Inv_Item("Pig Egg", 1, "consumable", 100)
]

automation = {
    "autofeeder_active" : False,
    "autofeed_type" : "Basic Food",
    "autowater_active" : False, 
    "funinator_active" : False
}
                
pets = []
inventory = [Inv_Item("Basic Food", 5, "feed", 5)]
money = 0

def menu(pets, money, inventory, shop, automation):
    if bool(pets):
        pets, money, inventory, automation = day(pets, inventory, money, shop, automation)
    else:
        pets = start()
        day(pets, inventory, money, shop, automation)

    return pets, money, inventory, automation

def addItemToInventory(inventory, itemToAdd):
    addedItem = False
    for i in inventory:
        if i.name == itemToAdd.name:
            i.amount += itemToAdd.amount
            addedItem = True
            break

    if not addedItem: inventory.append(itemToAdd)
    return inventory

def removeItemFromInventorY(inventory, itemToRemove):
    for i in inventory:
        if i.name == itemToRemove.name:
            i.amount -= 1
            break

    if itemToRemove.amount <= 0: inventory.remove(itemToRemove)

    return inventory

def goToShop(inventory, shop, money):
    names = []
    nameItemRef={}
    for i in shop: 
        print(i)
        names.append(i.name)
        nameItemRef[i.name] = i
    print(" ")
    names.append("quit")

    while True:
        print(f"You have ${money}")
        itemToBuy = idiot_proof_specific("Type the name of the item you would like to buy.\nType 'quit' to leave the menu: ", names)
        if itemToBuy != "quit": 
            if nameItemRef[itemToBuy].type == "feed" and not "Infinite" in itemToBuy: amount = idiot_proof_general("How many do you want to buy? ")
            else: amount = 1

        if itemToBuy == 'quit': break

        if nameItemRef[itemToBuy].shop_price * amount > money:
            print("You are too poor to buy that. Womp womp.")
            continue

        if not idiot_proof_yes_no(f"Are you sure you want to buy {amount} {itemToBuy}? "): continue

        money -= nameItemRef[itemToBuy].shop_price * amount
        item = nameItemRef[itemToBuy]
        item.amount = amount
        inventory = addItemToInventory(inventory, item)
        print(" ")

    return inventory, money

def day(pets, inventory, money, shop, automation):
    print("The day begins\n")
    for i in pets: i.day_stat_change()

    if automation["autofeeder_active"]:
            infinite = False
            hasFood = False
            failed = False
            for p in pets:
                if p.awake and p.alive:
                    for i in inventory:
                        if automation["autofeed_type"] == i.name: hasFood = True
                        if automation["autofeed_type"] == i.name.replace("Infinite ", "") and "Infinite" in i.name: 
                            infinite = True
                            hasFood = True

                        if hasFood:
                            p.autoFeed(automation["autofeed_type"])
                            if not infinite: inventory = removeItemFromInventorY(inventory, i)
                            print(f"Fed {p.name}")
                        else:
                            print("You didn't have enough food for the autofeeder")
                            failed = True
                            break
                    if failed: break

    if automation["autowater_active"]:
        for i in pets:
            if i.awake and i.alive: i.water()
    if automation["funinator_active"]:
            for i in pets:
                if i.awake and i.alive: i.play()
    print(" ")

    while True:
        print("1. Interact with pets")
        print("2. Go to market")
        print("3. Look at inventory")
        print("4. Use an item")
        print("5. Configure Auto-feeder")
        print("6. Send pigs to work and end the day")
        print("7. End the day without working the pigs")
        print(" ")
        option = idiot_proof_num_range("Enter the number of the desired option ", 1, 7)
        match option:
            case 1:
                while True:
                    validPets = []
                    print(" ")
                    for i in pets: 
                        
                        if i.alive and i.awake and not i.interacted:
                            validPets.append(i)
                            print(i.basic_print())

                    if not bool(validPets): 
                        print("You can't interact with any pets right now")
                        break

                    currentPet = 0
                    while True:
                        pet = idiot_proof_specific("What pet would you like to interact with? ", get_pet_names(validPets))
                        print(" ")
                        if pets[get_pet_index(pet, pets)].awake and pets[get_pet_index(pet, pets)].alive:
                            currentPet = get_pet_index(pet, pets)
                            break
                        else:
                            if not pets[get_pet_index(pet, pets)].alive: print("That pet is dead")
                            elif not pets[get_pet_index(pet, pets)].awake: print("That pet is sleeping")
                            elif pets[get_pet_index(pet, pets)].interacted: print("You already interacted with that pet today")
                    pets[currentPet].print_status()
                    pets[currentPet].interaction_options(inventory)
                    if not idiot_proof_yes_no("Would you like to interact with another pet? "): 
                        print("You can't interact with any pets right now")
                        print(" ")
                        break
            case 2:
                inventory, money = goToShop(inventory, shop, money)
            case 3:
                printInventory(inventory)
            case 4:
                inventory, pets, automation = useItem(inventory, pets, automation)
            case 5:
                automation = AutofeedConfig(automation)
            case 6:
                print("Your pigs are digging for truffles")
                money += getMone(pets)
                for i in pets: 
                    if i.alive: 
                        i.age += 1
                        i.energy -= 20
                saveData(pets, inventory, automation, money)          
                return pets, money, inventory, automation          
            case 7:
                for i in pets: 
                    if i.alive: 
                        i.age += 1
                        i.energy += 30
                        i.happiness += 25
                saveData(pets, inventory, automation, money)             
                return pets, money, inventory, automation


def AutofeedConfig(automation):
    if automation["autofeeder_active"]:
        print("1. Basic Food")
        print("2. Super Food")
        print("3. Wet Food")
        print("4. Medicinal Food")
        print("5. Tasty Food")
        option = idiot_proof_num_range(f"What food would you like to switch to (current food: {automation["autofeed_type"]})", 1, 5)

        match option:
            case 1: automation["autofeed_type"] = "Basic Food"
            case 2: automation["autofeed_type"] = "Super Food"
            case 3: automation["autofeed_type"] = "Wet Food"
            case 4: automation["autofeed_type"] = "Medicinal Food"
            case 5: automation["autofeed_type"] = "Tasty Food"
    else:
        print("You dont have an autofeeder. Buy one at the shop and remember to activate it.")

    return automation

def useItem(inventory, pets, automation):
    useable = False
    useables = []
    nameItemRef = {}
    for i in inventory:
        if i.type == "consumable":
            print(f"You have {i.amount} {i.name}(s)")
            useable = True
            useables.append(i.name)
            nameItemRef[i.name] = i

    if useable:
        use = idiot_proof_specific("What item do you want to use? ", useables)
        if use == "Pig Egg":
            pets.append(new_pet())
        if use == "Auto-feeder":
            automation["autofeeder_active"] = True
        if use == "Auto-water":
            automation["autowater_active"] = True
        if use == "The Funinator":
            automation["funinator_active"] = True
        
        inventory = removeItemFromInventorY(inventory, nameItemRef[use])
        return inventory, pets, automation
    else:
        print("You have nothing that can be used")
        return inventory, pets, automation

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
    
def printInventory(inventory):
    if bool(inventory):
        for i in inventory:
            print(f"You have {i.amount} {i.name}(s)")

        input("Hit enter to continue")
    else:
        print("You don't own anything poor u")

def getMone(pets):
    total = 0
    for i in pets:
        if i.awake and i.alive:
            chance = i.skill + randint(0, 100)
            total += getAmount(chance)

    print(f"You earned ${total} today")
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
    print("You got a new pig!")
    sleep(0.5)
    name = input_cool("What would you like to name your pig? ")
    print(f"You now have a new pig named {name}!")
    return Pet(name)

def start():
    print("Welcome to Pakistans Slave Labor Simulator!")
    sleep(1)
    print("I mean, welcome to Pakistans Pig Farm Simulator!")
    sleep(0.5)
    print("Of course")
    sleep(0.5)
    print_cool("...",0.5)
    sleep(1)
    print("Anyway, lets get you started")
    print("I'm giving you this stater pig for free, but don't expect any more charity outta me")
    print("You know, like, inflation, or something")
    print("Make sure it doesn't die, and don't overwork it")
    print("Good luck, I guess")
    sleep(2)
    return [new_pet()]

def fast_start():
    return [Pet("Jorp")]

def saveData(pets, inventory, automation, money):
    # Saves pet data
    if os.path.isfile("Practices/Pakistans Slave Labor Simulator/pet_saves.json"):
        with open("Practices/Pakistans Slave Labor Simulator/pet_saves.json", "w") as jFile:
            petData = []
            for i in pets: 
                petData.append(i.__dict__)

            json.dump(petData, jFile, indent=4)
    else:
        raise Exception("No file found dingus")
    
    # Saves inventory data
    if os.path.isfile("Practices/Pakistans Slave Labor Simulator/inventory_saves.json"):
        with open("Practices/Pakistans Slave Labor Simulator/inventory_saves.json", "w") as file:
            invData = []
            for i in inventory: 
                invData.append(i.__dict__)

            json.dump(invData, file, indent=4)
    else:
        raise Exception("No file found dingus")

    # Saves money and automation
    if os.path.isfile("Practices/Pakistans Slave Labor Simulator/save_data.json"):
        with open("Practices/Pakistans Slave Labor Simulator/save_data.json", "w") as file:
            data = {
                "money" : money,
                "automation" : automation
            }

            json.dump(data, file, indent=4)
    else:
        raise Exception("No file found dingus")

def loadData():
    outPets = []
    outInv = []
    outMoney = 0
    outAuto = {}
    # Loads pet data
    if os.path.isfile("Practices/Pakistans Slave Labor Simulator/pet_saves.json"):
        try:
            with open("Practices/Pakistans Slave Labor Simulator/pet_saves.json", "r") as jFile:
                jsonData = json.load(jFile)
                petDataRaw = []
                petData = []

                for i in jsonData: 
                    petDataRaw.append(i)

                for i in petDataRaw:
                    newPet = Pet(i["name"])
                    newPet.age = i["age"]
                    newPet.hunger = i["hunger"]
                    newPet.thirst = i["thirst"]
                    newPet.health = i["health"]
                    newPet.happiness = i["happiness"]
                    newPet.energy = i["energy"]
                    newPet.awake = i["awake"]
                    newPet.alive = i["alive"]
                    newPet.skill = i["skill"]

                    petData.append(newPet)
                outPets = petData
        except json.JSONDecodeError:
            outPets = []
    
    # Loads inventory data
    if os.path.isfile("Practices/Pakistans Slave Labor Simulator/inventory_saves.json"):
        try:
            with open("Practices/Pakistans Slave Labor Simulator/inventory_saves.json", "r") as jFile:
                jsonData = json.load(jFile)
                invDataRaw = []
                invData = []

                for i in jsonData: 
                    invDataRaw.append(i)

                for i in invDataRaw:
                    invItem = Inv_Item(i["name"], i["amount"], i["type"], i["shop_price"])
                    invData.append(invItem)

                outInv = invData
        except json.JSONDecodeError:
            outInv = [Inv_Item("Basic Food", 5, "feed", 5)]
    
    # Loads money and automation
    if os.path.isfile("Practices/Pakistans Slave Labor Simulator/save_data.json"):
        try:
            with open("Practices/Pakistans Slave Labor Simulator/save_data.json", "r") as jFile:
                jsonData = json.load(jFile)

                outMoney = jsonData["money"]
                outAuto = jsonData["automation"]
        except json.JSONDecodeError:
            outMoney = 0
            outAuto = {
                "autofeeder_active" : False,
                "autofeed_type" : "Basic Food",
                "autowater_active" : False, 
                "funinator_active" : False
            }

    return outPets, outInv, outMoney, outAuto

if not idiot_proof_yes_no("Would you like to delete your old save and start fresh? "): pets, inventory, money, automation = loadData()
else:
    with open("Practices/Pakistans Slave Labor Simulator/pet_saves.json", "w") as file:
        file.write("")
    with open("Practices/Pakistans Slave Labor Simulator/inventory_saves.json", "w") as file:
        file.write("")
    with open("Practices/Pakistans Slave Labor Simulator/save_data.json", "w") as file:
        file.write("")

money = 0

while True:
    pets, money, inventory, automation = menu(pets, money, inventory, shop, automation)