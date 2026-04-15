from random import randint, choice
from time import sleep
from copy import copy

class Enemy:
    def __init__(self, name, weaponOne, weaponTwo, weaponThree, health):
        self.name = name
        self.weaponOne = weaponOne
        self.weaponTwo = weaponTwo
        self.weaponThree = weaponThree
        self.health = health
        
class Weapon:
    def __init__(self, damageMin, damageMax, shots, hitChance, installSkill):
        self.damageMin = damageMin
        self.damageMax = damageMax
        self.shots = shots
        self.hitChance = hitChance
        self.installSkill = installSkill

class Item:
    def __init__(self, name, amount, weight, type, rarity):
        self.name = name
        self.amount = amount
        self.weight = weight
        self.type = type
        self.rarity = rarity		

def run_GTC(root):
    root.destroy()
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    WHITE = '\033[37m'
    RESET = "\033[0m"

    worldWidth = 3
    worldLength = 100

    playerPos = 0
    playerRoad = 0

    carHealth = 27
    maxHealth = 30
    gas = 27
    maxGas = 30
    mechanicsSkill = 4

    speed = 1

    world = {}
    exits = {}
    turns = {}
    enemies = {}

    inventory = []
    equippedWeapons = ["none", "none", "none"]

    itemTable = {
        "scrap" : Item("scrap", 1, 1, "scrap", "common"),
        "advanced scrap" : Item("advanced scrap", 1, 3, "scrap", "epic"),
        "small gas canister" : Item("small gas canister", 1, 5, "consumable", "common"),
        "medium gas canister" : Item("medium gas canister", 1, 10, "consumable", "rare"),
        "large gas canister" : Item("large gas canister", 1, 15, "consumable", "epic"),
        "beginner mechanics manual" : Item("beginner mechanics manual", 1, 3, "consumable", "common"),
        "intermediate mechanics manual" : Item("intermediate mechanics manual", 1, 5, "consumable", "rare"),
        "advanced mechanics manual" : Item("advanced mechanics manual", 1, 8, "consumable", "epic"),
        "steel plate" : Item("steel plate", 1, 4, "consumable", "common"),
        "reinforced steel plate" : Item("reinforced steel plate", 1, 6, "consumable", "rare"),
        "diamond-steel plate" : Item("diamond-steel plate", 1, 9, "consumable", "legendary"),
        "potato launcher" : Item("potato launcher", 1, 7, "weapon", "common"),
        "plank" : Item("plank", 1, 6, "weapon", "common"),
        "paintball gun" : Item("paintball gun", 1, 6, "weapon", "common"),
        "box of nails" : Item("box of nails", 1, 4, "weapon", "common"),
        "air fryer" : Item("air fryer", 1, 9, "weapon", "common"),
        "shotgun" : Item("shotgun", 1, 9, "weapon", "rare"),
        "harpoon launcher" : Item("harpoon launcher", 1, 12, "weapon", "rare"),
        "brick catapult" : Item("brick catapult", 1, 11, "weapon", "rare"),
        "spear" : Item("spear", 1, 13, "weapon", "rare"),
        "sniper rifle" : Item("sniper rifle", 1, 15, "weapon", "epic"),
        "minigun" : Item("minigun", 1, 18, "weapon", "epic"),
        "flamethrower" : Item("flamethrower", 1, 16, "weapon", "epic"),
        "lazer cannon" : Item("lazer cannon", 1, 20, "weapon", "legendary"),
        "VMARPG" : Item("VMARPG", 1, 23, "weapon", "legendary"),
        "engine booster" : Item("engine booster", 1, 3, "consumable", "rare"),
        "engine supercharger" : Item("engine supercharger", 1, 5, "consumable", "legendary"),
        "gasoline compressor" : Item("gasoline compressor", 1, 5, "consumable", "rare"),
        "gasoline miniaturizer" : Item("gasoline miniaturizer", 1, 8, "consumable", "legendary"),
    }

    lootTable = {
        "scrap" : 30,
        "advanced scrap" : 10,
        "small gas canister" : 30,
        "medium gas canister" : 10,
        "large gas canister" : 5,
        "beginner mechanics manual" : 30,
        "intermediate mechanics manual" : 15,
        "advanced mechanics manual" : 6,
        "steel plate" : 20,
        "reinforced steel plate" : 7,
        "diamond-steel plate" : 2,
        "potato launcher" : 12,
        "plank" : 11,
        "paintball gun" : 12,
        "box of nails" : 11,
        "air fryer" : 10,
        "shotgun" : 6,
        "harpoon launcher" : 7,
        "brick catapult" : 6,
        "spear" : 5,
        "sniper rifle" : 3,
        "minigun" : 3,
        "flamethrower" : 3,
        "lazer cannon" : 1,
        "VMARPG" : 1,
        "engine booster" : 15,
        "engine supercharger" : 3,
        "gasoline compressor" : 5,
        "gasoline miniaturizer" : 1,
    }

    weapons = {
        "potato launcher" : Weapon(3, 5, 1, 75, 5),
        "plank" : Weapon(8, 10, 1, 45, 6),
        "paintball gun" : Weapon(1, 2, 8, 60, 7),
        "box of nails" : Weapon(1, 2, 25, 10, 8),
        "air fryer" : Weapon(20, 22, 1, 25, 9),
        "shotgun" : Weapon(3, 8, 7, 50, 15),
        "harpoon launcher" : Weapon(30, 38, 1, 45, 17),
        "brick catapult" : Weapon(5, 15, 3, 50, 19),
        "spear" : Weapon(15, 25, 1, 97, 21),
        "sniper rifle" : Weapon(30, 50, 1, 98, 30),
        "minigun" : Weapon(2, 10, 20, 55, 33),
        "flamethrower" : Weapon(2, 30, 3, 66, 36),
        "lazer cannon" : Weapon(1, 3, 50, 75, 50),
        "VMARPG" : Weapon(100, 250, 1, 25, 60),
        "Semi Cannon" : Weapon(50, 125, 1, 20, 0),
        "Semi Blaster" : Weapon(1, 2, 35, 70, 0),
        "Semi Energizer" : Weapon(1, 100, 3, 50, 0)
    }

    itemDefinitions = {
        "scrap" : "A jumble of scrap metal. Recovers three health points.",
        "advanced scrap" : "A pile of extremely high-quality material. Recovers thirty health points",
        "small gas canister" : "A little contaner of gas. Worth three gas points",
        "medium gas canister" : "A decently sized container of gas. Worth seven gas points",
        "large gas canister" : "An absolutely massive container of gas. Worth twelve gas points",
        "beginner mechanics manual" : "A basic mechanics handbook. Gives one skill",
        "intermediate mechanics manual" : "A more in-depth and advanced mechanics handbook. Gives 3 skill",
        "advanced mechanics manual" : "A highly in-depth mechanics manual, mostly for professionals. Gives 6 skill",
        "steel plate" : "A basic steel plate. Gives your car an additional 5 hp",
        "reinforced steel plate" : "A high-strength, heavy duty steel plate. Gives your car an additional 15 hp",
        "diamond-steel plate" : "An over-the-top, rediculously strong steel plate. Gives your car an additional 45 hp",
        "potato launcher" : "An air-powered potato cannon. Damage: 3-5, Shots: 1, Hit chance: 75, Install skill: 5",
        "plank" : "A piece of wood. Damage: 8-10, Shots: 1, Hit chance: 45, Install skill: 6",
        "paintball gun" : "Very painful. Damage: 1-2, Shots: 8, Hit chance: 60, Install skill: 7",
        "box of nails" : "Tetanus inducing grapeshot weapon. Damage: 1-2, Shots: 25, Hit chance: 10, Install skill: 8",
        "air fryer" : "Cooks food using the air. Damage: 20-22, Shots: 1, Hit chance: 25, Install skill: 9",
        "shotgun" : "Shoots projectiles in a large spread. Damage: 3-8, Shots: 7, Hit chance: 50, Install skill: 15",
        "harpoon launcher" : "Fires a big'ol harpoon. Damage: 30-38, Shots: 1, Hit chance: 45, Install skill: 17",
        "brick catapult" : "Launches many pain rectangles. Damage: 5-15, Shots: 3, Hit chance: 50, Install skill: 19",
        "spear" : "A long-range stabby boi. Damage: 15-25, Shots: 1, Hit chance: 97, Install skill: 21",
        "sniper rifle" : "Fires at enemies with extreme precision. Damage: 30-50, Shots: 1, Hit chance: 98, Install skill: 30",
        "minigun" : "Agressively fast firearm. Damage: 2-10, Shots: 20, Hit chance: 55, Install skill: 33",
        "flamethrower" : "THIS THING SHOOT FIRE!!!! Damage: 2-30, Shots: 3, Hit chance: 66, Install skill: 36",
        "lazer cannon" : "Evaporates foes instantly. Damage: 1-3, Shots: 50, Hit chance: 75, Install skill: 50",
        "VMARPG" : "Eradicates anything it hits. Damage: 100-250, Shots: 1, Hit chance: 15, Install skill: 60", 
        "engine booster" : "A powerful engine fluid that boosts the engine when mixed with gas. Increases miles per turn by 10",
        "engine supercharger" : "An illegal engine boosting fluid that causes intense reactions when lit. Increases miles per turn by 30",
        "gasoline compressor" : "An interesting chemical concoction that increases the density of gas, thereby shrinking it. Increases max gas by 5",
        "gasoline miniaturizer" : "A powerful fluid that compresses the atoms in gas significantly. Increases max gas by 15 ",
    }

    enemyWeaponChancesEasy = {
        "potato launcher" : 25,
        "plank" : 20,
        "paintball gun" : 10,
        "box of nails" : 15,
        "air fryer" : 10,
    }

    enemyWeaponChancesMedium = {
        "potato launcher" : 10,
        "plank" : 10,
        "paintball gun" : 10,
        "box of nails" : 10,
        "air fryer" : 10,
        "shotgun" : 10,
        "harpoon launcher" : 7,
        "brick catapult" : 7,
        "spear" : 7,
        "sniper rifle" : 2,
        "minigun" : 2,
        "flamethrower" : 2,
    }

    enemyWeaponChancesHard = {
        "potato launcher" : 5,
        "plank" : 5,
        "paintball gun" : 5,
        "box of nails" : 5,
        "air fryer" : 5,
        "shotgun" : 10,
        "harpoon launcher" : 10,
        "brick catapult" : 10,
        "spear" : 10,
        "sniper rifle" : 5,
        "minigun" : 5,
        "flamethrower" : 5,
        "lazer cannon" : 2,
        "VMARPG" : 2,
    }

    enemyWeaponChancesInsane = {
        "shotgun" : 5,
        "harpoon launcher" : 5,
        "brick catapult" : 5,
        "spear" : 5,
        "sniper rifle" : 10,
        "minigun" : 10,
        "flamethrower" : 10,
        "lazer cannon" : 5,
        "VMARPG" : 5,
    }

    names = ["Tesla Model X", "Dodge Challenger", "Chevorlet Nova", "Toyata Corrola", "Dodge Caravan"]

    parsedEnemyWeaponChancesEasy = []
    parsedEnemyWeaponChancesMedium = []
    parsedEnemyWeaponChancesHard = []
    parsedEnemyWeaponChancesInsane = []

    for i in enemyWeaponChancesEasy.keys():
        for j in range(enemyWeaponChancesEasy[i]):
            parsedEnemyWeaponChancesEasy.append(i)

    for i in enemyWeaponChancesMedium.keys():
        for j in range(enemyWeaponChancesMedium[i]):
            parsedEnemyWeaponChancesMedium.append(i)

    for i in enemyWeaponChancesHard.keys():
        for j in range(enemyWeaponChancesHard[i]):
            parsedEnemyWeaponChancesHard.append(i)

    for i in enemyWeaponChancesInsane.keys():
        for j in range(enemyWeaponChancesInsane[i]):
            parsedEnemyWeaponChancesInsane.append(i)

    parsedLootTable = []
    for i in lootTable.keys():
        for j in range(lootTable[i]):
            parsedLootTable.append(i)

    def randomBool(trueChance):
        randomNum = randint(0, 100)
        return randomNum <= trueChance

    def worldGen(worldWidth, worldLength, parsedLootTable, parsedEnemyWeaponChancesEasy, parsedEnemyWeaponChancesMedium, parsedEnemyWeaponChancesHard, parsedEnemyWeaponChancesInsane, names):
        world = {}
        turns = {}
        exits = {}
        enemies = {}

        for i in range(-worldWidth, worldWidth + 1):
            for j in range(worldLength):
                if randomBool(15):
                    world[(j, i)] = "exit"
                    exits[(j, i)] = exit(parsedLootTable)
                elif randomBool(20):
                    world[(j, i)] = "turn"
                    turns[(j, i)] = turn(i, worldWidth)
                else:
                    world[(j, i)] = "empty"
                    if randomBool(35):
                        enemies[(j, i)] = createEnemy(parsedEnemyWeaponChancesEasy, parsedEnemyWeaponChancesMedium, parsedEnemyWeaponChancesHard, parsedEnemyWeaponChancesInsane, j, names)
                    else:
                        enemies[(j, i)] = "empty"

        enemies[(0, 0)] = "empty"
        enemies[(100, 0)] = Enemy("Super Semi", "Semi Blaster", "Semi Blaster", "Semi Energizer", 250)
        world[(0, 0)] = "empty"
        world[(100, 0)] = "empty"
        world[(2, 0)] = "exit"
        world[(1, 0)] = "empty"
        enemies[(1, 0)] = "empty"
        exits[(2, 0)] = [[], ["plank", "scrap", "beginner mechanics manual", "box of nails"], ["air fryer", "scrap", "steel plate", "steel plate", "paintball gun"], ["steel plate", "medium gas canister", "intermediate mechanics manual",  "reinforced steel plate"]]
        return world, exits, turns, enemies
    
    def exit(parsedLootTable):
        newList = []
    
        for i in range(4):
            localLoot = []
            lootCount = randint(3, 7)
            for i in range(lootCount):
                localLoot.append(choice(parsedLootTable))

            newList.append(localLoot)
        return newList

    def turn(turns, worldWidth) :
        listy = [-1, 1]
        number = 0
        if turns == -worldWidth:
            number = 1
        elif turns == worldWidth:
            number = -1
        else:
            number = choice(listy)
    
        moveOut = turns + number
        return moveOut 

    def createEnemy(easyList, mediumList, hardList, insaneList, distance, names):
        if distance <= 25:
            weapOne = choice(easyList)
            weapTwo = choice(easyList)
            weapThree = choice(easyList)
        elif distance <= 50:
            weapOne = choice(mediumList)
            weapTwo = choice(mediumList)
            weapThree = choice(mediumList)
        elif distance <= 75:
            weapOne = choice(hardList)
            weapTwo = choice(hardList)
            weapThree = choice(hardList)
        else:
            weapOne = choice(insaneList)
            weapTwo = choice(insaneList)
            weapThree = choice(insaneList)

        health = randint(1, 5) * (distance + 1)
        name = choice(names)

        return Enemy(name, weapOne, weapTwo, weapThree, health)

    world, exits, turns, enemies = worldGen(worldWidth, worldLength, parsedLootTable, parsedEnemyWeaponChancesEasy, parsedEnemyWeaponChancesMedium, parsedEnemyWeaponChancesHard, parsedEnemyWeaponChancesInsane, names)

    def checkInventory(inventory):
        for i in inventory:
            if i.amount <= 0:
                inventory.remove(i)

        return inventory

    def itemDictionary(itemDefs):
        YELLOW
        RESET

        while True:
            print(" ")
            itemToLookup = input("What item do you want to define? Type the name of the item or 'quit' to exit ")

            while not itemToLookup in itemDefs.keys() and itemToLookup != "quit":
                print("That's not a real item")
                itemToLookup = input("What item do you want to define")

            if itemToLookup == 'quit':
                break
            
            print(" ")
            print(f"{YELLOW}{itemToLookup}: {itemDefs[itemToLookup]}{RESET}")


    def PlayerTurn(world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, turns, speed):	
        sleep(1)
        gas -= 2
        print(" ")
        print(f"You are now at mile {BLUE}{playerPos * 10}{RESET}")
        print(f"You have {BLUE}{gas}{RESET} liters of gas remaining")
        print(" ")
    

        if gas <= 0:
            print(f"{RED}You are out of gas.{RESET}")
            print(f"{RED}If you are still out of gas at the end of the turn, you will die{RESET}")
            sleep(3)

        possibleInputs = ["1", "2", "3", "4", "5", "6", "7"]

        while True:
            print(" ")
            print("Do you want to \n 1. Look at your inventory \n 2. Look at your equipped weapons \n 3. Use the item dictionary \n 4. Use an item \n 5. Make repairs \n 6. Equip new weapons \n 7. Continue")
            turnInput = input("Type the number of the option. ")	

            while not turnInput in possibleInputs:
                print("That is not a valid option")
                turnInput = input("Pick a number between one and seven ")	

            print(" ")
            if turnInput == "1":
                if bool(inventory):
                    for i in inventory:
                            if i.rarity == "rare": color = BLUE 
                            elif i.rarity == "epic": color = PURPLE 
                            elif i.rarity == "legendary": color = YELLOW 
                            else: color = WHITE
                            print(f"{color}You have {i.amount} {i.name}(s){RESET}")

                    input("Type anything to continue")
                else:
                    print("Your inventory is empty")
            elif turnInput == "2":
                for i in range(len(equippedWeapons)):
                    if equippedWeapons[i] == "none":
                        print(f"There is nothing equipped in slot {i}")
                    else:
                        weaponItem = itemTable[equippedWeapons[i]]
                        if weaponItem.rarity == "rare": color = BLUE 
                        elif weaponItem.rarity == "epic": color = PURPLE 
                        elif weaponItem.rarity == "legendary": color = YELLOW 
                        else: color = WHITE
                        print(f"There is a {equippedWeapons[i]} in slot {i + 1}")
            elif turnInput == "3":
                itemDictionary(itemDefs)
            elif turnInput == "4":
                gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas = useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth, speed)
            elif turnInput == "5":
                if gas < maxGas:
                    inventory, health = makeRepairs(inventory, health, maxHealth)
                else:
                    print("Your car is already at max health")
            elif turnInput == "6":
                inventory, equippedWeapons = modCar(inventory, equippedWeapons, weaponDict, mechanicsSkill)
            elif turnInput == "7":
                if gas <= 0:
                    print(f"{RED}You are still out of gas{RESET}")
                    sleep(2)
                    print(f"{RED}Since you cant escape, cars quickly find you.{RESET}")
                    sleep(2)
                    print(f"{RED}You do not survive{RESET}")
                    sleep(2)
                    return world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, False, speed
                break

            sleep(2)

        if world[(playerPos, playerRoad)] == "exit":
            print(f"{YELLOW}You reach an exit{RESET}")
            inventory, exits = DoExit(playerPos, playerRoad, exits, itemDefs, itemTable, inventory)
        elif world[(playerPos, playerRoad)] == "turn":
            print(" ")
            print("You reached a turn")

            turnInput = input(f"Do you want to turn to road {turns[(playerPos, playerRoad)]}?")

            while turnInput != "yes" and turnInput != "no":
                print("That input is invalid")
                turnInput = input(f"Do you want to turn to road {playerRoad + turns[(playerPos, playerRoad)]}?")

            if turnInput == "yes": DoTurn(playerPos, playerRoad, turns)
    
        if world[(playerPos, playerRoad)] == "empty" and enemies[(playerPos, playerRoad)] != "empty":
            print(f"{RED}You encounter an enemy!{RESET}")
            sleep(1)
            health, enemies, cont = DoCombat(enemies[(playerPos,playerRoad)], health, maxHealth, equippedWeapons, weaponDict, playerPos, playerRoad, enemies)
            if inventory == None:
                inventory = []

            if playerPos >= 100 and not cont:
                Victory()
                return True, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, not cont, speed
    
            if cont == True: return world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, False, speed

        stopInput = False
        driveAmount = 1
        if speed > 1 and (playerPos + speed) < 100:
            for i in range(1, speed - 1):
                if world[(playerPos + i, playerRoad)] == "exit":
                    print(f"There is an exit in {i * 10} miles")
                    stopInput = input("Do you want to stop here?")

                    while stopInput != "yes" and stopInput != "no" and stopInput != "y" and stopInput != "n":
                        print("Answer 'yes' or 'no'")
                        stopInput = input("Do you want to stop at the exit?")

                    if stopInput == "yes" or stopInput == "y":
                        stopInput = True
                        driveAmount = i
                        break
                    else:
                        stopInput = False
                elif world[(playerPos + i, playerRoad)] == "turn":
                    print(f"There is a turn in {i * 10} miles")
                    stopInput = input("Do you want to stop here?")

                    while stopInput != "yes" and stopInput != "no" and stopInput != "y" and stopInput != "n":
                        print("Answer 'yes' or 'no'")
                        stopInput = input("Do you want to stop at the turn?")

                    if stopInput == "yes" or stopInput == "y":
                        stopInput = True
                        driveAmount = i
                        break
                    else:
                        stopInput = False

        if stopInput == False: playerPos += speed
        else: playerPos += driveAmount

        if playerPos >= 100:
            playerPos = 100
            playerRoad = 0

            print("You have reached the border")
            sleep(1)
            print(f"{RED}Only one foe remains{RESET}")
            sleep(4)
            return world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, True, speed

        if inventory == None:
            inventory = []
        print("You continue driving")
        return world, playerRoad, playerPos, enemies, health, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, True, speed

    def calcWeaponDamage(name, weaponDict):
        totalDamage = 0
        weapon = weaponDict[name]

        hitCount = 0
        for i in range(weapon.shots):
            if randomBool(weapon.hitChance):
                damage = randint(weapon.damageMin, weapon.damageMax)
                hitCount += 1
                totalDamage += damage


        print(f"The {name} hit {hitCount} times and dealt {totalDamage} damage")
        return totalDamage
    
    
    def DoCombat(enemy, health, maxHealth, playerWeapons, weaponTable, playerPos, playerRoad, enemyDict): # the bool returned is telling playerTurn if the player is dead or not
        RED
        YELLOW
        RESET
        enemyWeapons = [enemy.weaponOne, enemy.weaponTwo, enemy.weaponThree]
        print(f"You are fighting a {enemy.name}")

        print(" ")

        for i in enemyWeapons:
            print(f"It has a(n) {i}")
    
        while True:
            print(" ")
            repairInput = input("Do you want to make repairs? 'yes' or 'no'. ")

            if health < maxHealth:
                while repairInput != "yes" and repairInput != "no":
                    print("That input is invalid")
                    repairInput = input("Do you want to make repairs? 'yes' or 'no'. ")

                if repairInput == "yes":
                    makeRepairs(inventory, health, maxHealth)

            attackInput = input("Do you want to 'attack' or 'dodge'? ")
            while attackInput != "attack" and attackInput != "dodge":
                print("That input is invalid")
                attackInput = input("Do you want to 'attack' or 'dodge'? ")

            if attackInput == "attack":
                totalDamage = 0
                for i in playerWeapons:
                    if i != "none":
                        weapon = weaponTable[i]
                        totalDamage += calcWeaponDamage(i, weaponTable)
                        sleep(1)

                enemy.health -= totalDamage
                print(f"You dealt {totalDamage} damage")

                if enemy.health > 0:
                    print(f"The {enemy.name} now has {enemy.health} HP")
                else:
                    if enemy.name != "Super Semi":
                        print(f"You killed the {enemy.name}")
                    else:
                        print(f"{YELLOW}You killed the Super Semi, the final obstacle between you and Canada{RESET}")
                    enemies[(playerPos, playerRoad)] = "empty" 
                    return health, enemyDict, False
            else:
                print("You avoid the enemies attack")
                continue

            sleep(2)
            print(" ")
            print("The enemy is attacking!")
            print(" ")

            enemyDamage = 0

            for i in enemyWeapons:
                weapon = weaponTable[i]
                enemyDamage += calcWeaponDamage(i, weaponTable)

            health -= enemyDamage
            print(f"The {enemy.name} did {enemyDamage} damage")

            if health > 0:
                print(f"You now have {health} HP")
            else:
                print(f"{RED}You died{RESET}")
                return health, enemyDict, True
    
    def Victory():
        YELLOW
        GREEN
        RESET

        victoryString = f"""{GREEN}
     _____      _     _____       _____                       _       
    |  __ \    | |   |_   _|     /  __ \                     | |      
    | |  \/ ___| |_    | | ___   | /  \/ __ _ _ __   __ _  __| | __ _ 
    | | __ / _ \ __|   | |/ _ \  | |    / _` | '_ \ / _` |/ _` |/ _` |
    | |_\ \  __/ |_    | | (_) | | \__/\ (_| | | | | (_| | (_| | (_| |
     \____/\___|\__|   \_/\___/   \____/\__,_|_| |_|\__,_|\__,_|\__,_|
    {RESET}"""
        print(" ")
        sleep(5)
        print(f"{YELLOW}You did it.{RESET}")
        sleep(2)
        print(f"{YELLOW}You made it to Canada.{RESET}")
        sleep(2)
        print(f"{YELLOW}You are a champion.{RESET}")
        sleep(5)
        print(victoryString)
        sleep(3)
        print(f"{GREEN}Made by Paxton Hall{RESET}")
        sleep(3)
        print(f"{GREEN}Thanks for playing!{RESET}")

    def DoExit(playerPos, playerRoad, exits, itemDefs, itemTable, inventory):
        YELLOW
        BLUE
        RED
        RESET
        WHITE

        exit = exits[playerPos, playerRoad]

        while True:
            print(" ")
            print("What building do you want to loot")
            loot = []

            buildingToLoot = input("Pick options '1', '2', or '3'. Type 'quit' to stop looting.")
            while buildingToLoot != '1' and buildingToLoot != '2'and buildingToLoot != '3' and buildingToLoot != 'quit':
                print("Invalid input")
                buildingToLoot = input("Pick options '1', '2', or '3'. Type 'quit' to stop looting.")

            if buildingToLoot == "quit":
                break

            buildingToLoot = int(buildingToLoot)

            for i in exit[buildingToLoot]:
                if itemTable[i].rarity == "rare": color = BLUE 
                elif itemTable[i].rarity == "epic": color = PURPLE 
                elif itemTable[i].rarity == "legendary": color = YELLOW 
                else: color = WHITE
                print(f"{color}There is a(n) {i}{RESET}")
                loot.append(i)

            while True:
                print(" ")
                if not bool(loot):
                    print("There is nothing in this building")
                    break

                itemToGrab = input("What item do you want to grab. Type the name of the item or 'quit' to leave this building. \nType 'def' to open the item definiton menu \nType 'all' to grab everything  ")

                while not itemToGrab in loot and itemToGrab != "quit" and itemToGrab != "def" and itemToGrab != 'all':
                    print("That item is not there")
                    itemToGrab = input("What item do you want to grab? Type the name of the item or 'quit' to exit. \nType 'def' to open the item definiton menu \nType 'all' to grab everything  ")

                if itemToGrab == "quit":
                    break
                elif itemToGrab == "def":
                    itemDictionary(itemDefs)
                    print("")
                    color = ""
                    for i in loot:
                        if itemTable[i].rarity == "rare": color = BLUE 
                        elif itemTable[i].rarity == "epic": color = PURPLE 
                        elif itemTable[i].rarity == "legendary": color = YELLOW 
                        else: color = WHITE
                        print(f"{color}There is a(n) {i} ({itemTable[i].type}){RESET} ")
                elif itemToGrab == "all":
                    print(" ")
                    print("You grab everything")

                    for i in loot:
                        inventory = AddItem(inventory, i, itemTable)
    
                    exit[buildingToLoot] = []
                    loot = []
                    break

                else:
                    print(" ")
                    print(f"You grab the {itemToGrab}")
                    exit[buildingToLoot].remove(itemToGrab)
                    loot.remove(itemToGrab)
                    inventory = AddItem(inventory, itemToGrab, itemTable)
                    print(" ")

                    for i in loot:
                        if itemTable[i].rarity == "rare": color = BLUE 
                        elif itemTable[i].rarity == "epic": color = PURPLE 
                        elif itemTable[i].rarity == "legendary": color = YELLOW 
                        else: color = WHITE
                        print(f"{color}There is a(n) {i}{RESET}")

        if playerPos == 2:
            print(" ")
            print(f"{BLUE}Now that you have an array of weapons and manuals, make sure to use them to upgrade your gear{RESET}")
            print(" ")
            sleep(3)

        return inventory, exits

    def AddItem(inventory, name, itemTable):
        existingNames = []
        nameIndex = {}

        for i in inventory:
            existingNames.append(i.name)
            nameIndex[i.name] = inventory.index(i)

        if name in existingNames:
            inventory[nameIndex[name]].amount += 1
        else:
            item = copy(itemTable[name])
            item.amount = 1
            inventory.append(item)

        return inventory

    def DoTurn(playerPos, playerRoad, turns):
        playerRoad += turns[(playerPos, playerRoad)]

        if playerRoad != 0: print(f"You move to subroad {playerRoad}")
        else: print("You are back on the i-35")

    def useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth, speed):	
        while True:
            print(" ")

            if inventory == None:
                print("your inventory is empty")
                return gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas
    
            items = {}
            nameIndex = {}
            indexName = {}
            index = 1
            for i in inventory:
                if i.type == "consumable":
                    items[i.name] = i
                    print(f"({index}). {i.amount} {i.name}(s)")
                    nameIndex[i.name] = inventory.index(i)
                    indexName[index] = i.name
                    index += 1

            if len(items) == 0:
                print("You have no useable items")
                return gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas

    
            itemToUse = input("What item do you want to use? Type the name or number of the item or 'quit' to exit: ")

            if itemToUse.isdecimal():
                if not float(itemToUse) in indexName.keys():
                    itemToUse = "Failed Number Check"

            while not itemToUse in items.keys() and itemToUse != "quit" and not itemToUse.isdecimal():
                print("You do not have that item")
                itemToUse = input("What item do you want to use? Type the name of the item or 'quit' to exit: ")

                if itemToUse.isdecimal():
                    if not float(itemToUse) in indexName.keys():
                        itemToUse = "Failed Number Check"

            print(" ")

            if itemToUse.isdecimal():
                if float(itemToUse) in indexName.keys():
                    itemToUse = indexName[float(itemToUse)]

            if itemToUse != "quit": print(f"You use the {itemToUse}")

            if itemToUse == "small gas canister":
                if gas < maxGas:
                    gas += 3
                    if gas > maxGas:
                        gas = maxGas
                    print(f"You now have {gas} gasoline in your tank")

                    inventory[nameIndex[itemToUse]].amount -= 1
                else: print("You already have maxium gas in your tank")
            elif itemToUse == "medium gas canister":
                if gas < maxGas:
                    gas += 7
                    if gas > maxGas:
                        gas = maxGas
                    print(f"You now have {gas} gasoline in your tank")

                    inventory[nameIndex[itemToUse]].amount -= 1
                else: print("You already have maxium gas in your tank")
            elif itemToUse == "large gas canister":
                if gas < maxGas:
                    gas += 12
                    if gas > maxGas:
                        gas = maxGas
                    print(f"You now have {gas} gasoline in your tank")

                    inventory[nameIndex[itemToUse]].amount -= 1
                else: print("You already have maxium gas in your tank")
            elif itemToUse == "beginner mechanics manual":
                mechanicsSkill += 1
                print(f"You now have {mechanicsSkill} mechanics skill.")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "intermediate mechanics manual":
                mechanicsSkill += 4
                print(f"You now have {mechanicsSkill} mechanics skill.")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "advanced mechanics manual":
                mechanicsSkill += 10
                print(f"You now have {mechanicsSkill} mechanics skill.")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "steel plate":
                maxHealth += 5
                health = maxHealth
                print(f"You now have {maxHealth} car health.")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "reinforced steel plate":
                maxHealth += 15
                health = maxHealth
                print(f"You now have {maxHealth} car health.")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "diamond-steel plate":
                maxHealth += 45
                health = maxHealth
                print(f"You now have {maxHealth} car health.")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "engine booster":
                speed += 1
                print(f"Miles per turn increased to {speed * 10}")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "engine supercharger":
                speed += 3
                print(f"Miles per turn increased to {speed * 10}")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "gasoline compressor":
                maxGas += 5
                print(f"Maximum gasoline increased to {maxGas} liters")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "gasoline miniaturizer":
                maxGas += 15
                print(f"Maximum gasoline increased to {maxGas} liters")
                inventory[nameIndex[itemToUse]].amount -= 1
            elif itemToUse == "quit":
                inventory = checkInventory(inventory)
                return gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas
    
            inventory = checkInventory(inventory)


    def makeRepairs(inventory, health, maxHealth):
        while True:
            items = {}
            nameIndex = {}

            if inventory == None:
                print("Your inventory is empty")
                return inventory, health

            for i in inventory:
                if i.type == "scrap":
                    items[i.name] = i
                    nameIndex[i.name] = inventory.index(i)
                    print(f"You have {i.amount} {i.name}")

            if len(items) <= 0:
                print("You have no scrap in your inventory")
                return inventory, health

            scrapToUse = input("What scrap do you want to use. Type 'scrap' or 'advanced scrap', or 'quit'to leave the menu ")

            while not scrapToUse in items.keys() and scrapToUse != "quit":
                print("You dont have that")
                scrapToUse = input("What scrap do you want to use. Type 'scrap' or 'advanced scrap', or 'quit'to leave the menu ")

            if scrapToUse == "quit":
                return inventory, health
    
            if scrapToUse == "scrap":
                if inventory[nameIndex[scrapToUse]].amount < 2:
                    health += 3
                    if health > maxHealth: health = maxHealth
                    print(f"Your health is now {health}")
                    inventory[nameIndex[scrapToUse]].amount -= 1
                else:
                    amountToUse = input(f"How many would you like to use. It can be a max of {inventory[nameIndex[scrapToUse]].amount}")

                    while True:
                        if amountToUse.isdigit():
                            if int(amountToUse) > inventory[nameIndex[scrapToUse]].amount:
                                print("You dont have that many")
                            else:
                                amountToUse = int(amountToUse)
                                break
                        else:
                            print("It has to be a number")
                        amountToUse = input(f"How many would you like to use. It can be a max of {inventory[nameIndex[scrapToUse]].amount}")
                    inventory[nameIndex[scrapToUse]].amount -= amountToUse
                    health += 3 * amountToUse
                    if health > maxHealth: health = maxHealth
                    print(f"Your health is now {health}")


            elif scrapToUse == "advanced scrap":
                health += 3
                if health > maxHealth: health = maxHealth
                print(f"Your health is now {health}")
                inventory[nameIndex[scrapToUse]].amount -= 1
    

            inventory = checkInventory(inventory)

    def modCar(inventory, equippedWeapons, weaponTable, mechanicsSkill):
        BLUE
        RESET
        YELLOW
        PURPLE
        GREEN
        while True:
            items = {}
            nameIndex = {}

            print(" ")

            if inventory== None:
                print("Your inventory is empty")
                return inventory, equippedWeapons

            for i in inventory:
                if i.type == "weapon":
                    color = ""
                    if i.rarity == "rare": color = BLUE 
                    elif i.rarity == "epic": color = PURPLE 
                    elif i.rarity == "legendary": color = YELLOW 
                    elif i.rarity == "common": color = GREEN
                    items[i.name] = i
                    weapon = weaponTable[i.name]
                    nameIndex[i.name] = inventory.index(i)
                    print(f"{color}You have {i.amount} {i.name}(s){RESET} [damage: {weapon.damageMin} - {weapon.damageMax}, shots: {weapon.shots}, hit chance: {weapon.hitChance}, install skill: {weapon.installSkill}]")

            if len(items) <= 0:
                print("You have no weapons in your inventory")
                return inventory, equippedWeapons

            weaponToEquip = input("What weapon do you want to equip.Type the name of the weapon or 'quit'to leave the menu ")

            while not weaponToEquip in items.keys() and weaponToEquip != "quit":
                print("You dont have that")
                weaponToEquip = input("What weapon do you want to equip.Type the name of the weapon or 'quit' to leave the menu ")

            if weaponToEquip == "quit":
                return inventory, equippedWeapons
    
            if weaponTable[weaponToEquip].installSkill > mechanicsSkill:
                print(" ")
                print(f"You dont have enough skill to install the {weaponToEquip}")
                print(f"You need {BLUE}{weaponTable[weaponToEquip].installSkill}{RESET} skill, but you only have {BLUE}{mechanicsSkill}{RESET}")
                continue

            print(f"What slot do you want to attach the {weaponToEquip} to?")
            slot = input("Type '1', '2', or '3'")

            while slot != "1" and slot != "2" and slot != "3":
                print("Invalid slot")
                slot = input("Type '1', '2', or '3'")
    
            print(" ")

            if equippedWeapons[int(slot) - 1] == "none":
                equippedWeapons[int(slot) - 1] = weaponToEquip
                print(f"{weaponToEquip} equipped to slot {slot}")
                inventory[nameIndex[weaponToEquip]].amount -= 1
            else:
                print(f"You already have a(n) {equippedWeapons[int(slot) - 1]} attached to slot {slot}")
                yesNo = input("Do you want to replace it? 'yes' or 'no'? ")
                while yesNo != "yes" and yesNo != "no":
                    print("Invalid answer")
                    yesNo = input(f"Do you want to replace the {equippedWeapons[int(slot) - 1]}? 'yes' or 'no'? ")

                if yesNo == "yes":
                    equippedWeapons[int(slot) - 1] =  weaponToEquip
                    inventory[nameIndex[weaponToEquip]].amount -= 1
                    print(f"{weaponToEquip} equipped to slot {slot}")

            inventory = checkInventory(inventory)

    def Tutorial(inventory, itemTable, health, maxHealth, gas, maxGas, mechanicsSkill, equippedWeapons, weaponTable, speed):
        RED
        RESET
        print(f"{RED}You need to get out of here...{RESET}")
        sleep(2)
        print(f"{RED}It's not safe anymore...{RESET}")
        sleep(2)

        print("All newer cars have become sentient and murderous. This happened worldwide.")
        sleep(2)
        print("You live in Laredo, Texas, and you own a crusty 2003 Chrysler PT that did not become sentient")
        sleep(2)
        print("As far as you know, you are the last American alive.")
        sleep(2)
        print("You learn that Canada is the last remaining stronghold against the cars")
        sleep(2)
        print("It will be a long drive, but you have a couple tricks up your sleeve to help you survive")
        sleep(2)
        print(" ")
        print("First you need to grab some supplies. You enter the garage.")

        loot = ["potato launcher", "scrap", "small gas canister", "beginner mechanics manual"]

        for i in loot:
            print(f"There is a(n) {i}")

        print(" ")
        print("Grab the small gas canister. You'll need fuel.")

        tutInput = input("Type 'small gas canister' to grab it ")
        while tutInput != "small gas canister":
            tutInput = input("No, you need to type 'small gas canister'. You're gonna need gas. ")

        AddItem(inventory, "small gas canister", itemTable)
        print("You grab the small gas canister")
        print(" ")
        sleep(2)
        print("Your car is a little damaged. You can use the scrap to repair it.")

        tutInput = input("Type 'scrap' to grab it ")
        while tutInput != "scrap":
            tutInput = input("No, you need to type 'scrap'. You should have a repaired car before going out. ")

        AddItem(inventory, "scrap", itemTable)
        print("You grab the scrap")
        print(" ")
        sleep(2)

        tutInput = input("Now repair your car. Type 'make repairs' to use the scrap ")

        while tutInput != "make repairs":
            tutInput = input("No, you need to type 'make repairs'. You should have a repaired car before going out. ")
    
        inventory, health = makeRepairs(inventory, health, maxHealth)

        while health != 30:
            print(" ")
            print("You were supposed to use the scrap.")
            sleep(2)
            inventory, health = makeRepairs(inventory, health, maxHealth)

        print(" ")
        print("You realize that your fuel tank is also not full. Use the gas canister to refuel ")
        tutInput = input("Type 'use item' to use the gas canister ")

        while tutInput != "use item":
            print("You shouldn't leave on a half full tank")
            tutInput = input("Type 'use item' to use the gas canister ")

        gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas = useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth, speed)

        while gas < 30:
            print(" ")
            print("You shouldn't leave on a half full tank")
            sleep(2)
            gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas = useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth, speed)

        print(" ")
        sleep(2)
        print("Grab the beginner mechanics manual. It will likely be useful.")

        tutInput = input("Type 'beginner mechanics manual' to grab it ")
        while tutInput != "beginner mechanics manual":
            tutInput = input("No, you need to type 'beginner mechanics manual'. It will be good to have. ")

        AddItem(inventory, "beginner mechanics manual", itemTable)
        print("You grab the beginner mechanics manual")
        print(" ")
        sleep(2)

        print("Now for the final step. You need to defend yourself.")

        tutInput = input("Type 'potato launcher' to grab it ")
        while tutInput != "potato launcher":
            tutInput = input("No, you need to type 'potato launcher'. You need to be able to fight back. ")

        AddItem(inventory, "potato launcher", itemTable)
        print("You grab the potato launcher")
        print(" ")
        sleep(2)

        print("After some closer examination, you relize you dont know how to install it")
        print("Your mechanics skill is too low.")
        print(f"You can use the mechanics manual to increase your skill from {BLUE}four{RESET} to {BLUE}five{RESET}")

        tutInput = input("Type 'use item' to use the mechanics manual ")

        while tutInput != "use item":
            print("You need to know how to equip the potato launcher")
            tutInput = input("Type 'use item' to use the mechanics manual ")

        gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas = useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth, speed)

        while mechanicsSkill < 5:
            print(" ")
            print("You should probably learn how to attach the potato launcher")
            sleep(2)
            gas, mechanicsSkill, inventory, health, maxHealth, speed, maxGas = useItem(inventory, gas, maxGas, mechanicsSkill, health, maxHealth, speed)

        print(" ")
        print(f"Now for the most important part. {YELLOW}Attach the potato launcher{RESET}")

        sleep(2)

        tutInput = input("Type 'modify car' to enter the weapon equip menu.")

        while tutInput != "modify car":
            print("It's dangerous out there. You'll need a weapon.")
            tutInput = input("Type 'modify car' to enter the weapon equip menu.")

        print(" ")
        inventory, equippedWeapons = modCar(inventory, equippedWeapons, weaponTable, mechanicsSkill)

        while equippedWeapons[0] == "none" and equippedWeapons[1] == "none" and equippedWeapons[2] == "none":
            print(" ")
            print("You should probably attach the potato launcher")
            sleep(2)
            inventory, equippedWeapons = modCar(inventory, equippedWeapons, weaponTable, mechanicsSkill)

        print("Fantastic. You are ready(ish) to go out into the world.")
        sleep(2)
        print("Before you go, some last words of advice")
        sleep(2)
        print(f"Make sure to stop at exits. They lead to towns, {YELLOW}which you can loot{RESET}")
        sleep(2)
        print(f"Turns lead to {YELLOW}different roads, with new loot for you to grab{RESET}")
        sleep(2)
        print(f"You will find {RED}enemies{RESET} on the road. Continuously upgrade your gear to fight them off")
        sleep(2)
        print(f"{YELLOW}Good luck{RESET}")
        return 32, health, equippedWeapons, mechanicsSkill

    print(" ")
    skipInput = input("Do you want to skip the starting scene/tutorial? \nYou probably shouldn't unless you've played before. ")

    while skipInput != "yes" and skipInput != "no":
        print("Answer 'yes' or 'no'")
        skipInput = input("Do you want to skip the starting scene/tutorial? \nYou probably shouldn't unless you've played before. ")

    if skipInput == "no":
        gas, health, equippedWeapons, mechanicsSkill = Tutorial(inventory, itemTable, carHealth, maxHealth, gas, maxGas, mechanicsSkill, equippedWeapons, weapons, speed)
    else:
        print("Skipping tutorial")
        gas = 32
        carHealth = 30
        equippedWeapons[0] = "potato launcher"
        mechanicsSkill = 5

    while True:
        world, playerRoad, playerPos, enemies, carHealth, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefs, exits, weaponDict, itemTable, cont, speed = PlayerTurn(world, playerRoad, playerPos, enemies, carHealth, maxHealth, gas, maxGas, mechanicsSkill, inventory, equippedWeapons, itemDefinitions, exits, weapons, itemTable, turns, speed)
        if not cont:
            print("You lose. Restart the program to try again")
            break

        if world == True:
            break