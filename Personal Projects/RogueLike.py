import pygame as py
from random import choice, randint

class Upgrade:
    def __init__(self, name, stat, amount, rarity, description):
        self.name = name
        self.stat = stat
        self.amount = amount
        self.rarity = rarity
        self.description = description

py.init()

potUpgradesRaw = [
    Upgrade("Vitality", "Max Health", 1, "common", "Increases Max Health by 1"),
    Upgrade("Big Vitality", "Max Health", 2, "rare", "Increases Max Health by 2"),
    Upgrade("Huge Vitality", "Max Health", 3, "epic", "Increases Max Health by 3"),
    Upgrade("Pakistinian Vitality", "Max Health", 5, "pakistinian", "Increases Max Health by 5"),
    Upgrade("Haste", "Player Speed", 1, "common", "Increases Speed by 1"),
    Upgrade("Quick", "Player Speed", 2, "rare", "Increases Speed by 2"),
    Upgrade("Lightning Fast", "Player Speed", 3, "epic", "Increases Speed by 3"),
    Upgrade("Speed of Pakistan", "Player Speed", 5, "pakistinian", "Increases Speed by 5"),
    Upgrade("Quick Hands", "Reload Time", 0.9, "common", "Increases Reload Speed"),
    Upgrade("Dexterous", "Reload Time", 0.8, "rare", "Greatly Increases Reload Speed"),
    Upgrade("Reloader", "Reload Time", 0.7, "epic", "Massively Increases Reload Speed"),
    Upgrade("Pakistinian Dexterity", "Reload Time", 0.55, "pakistinian", "Increases Reload Speed to an Unreasonable Degree"),
    Upgrade("Full Heal", "Full Heal", 0, "common", "Recovers All Health"),
    Upgrade("Better Gunpowder", "Bullet Speed", 2, "common", "Increases Bullet Speed"),
    Upgrade("Boom Juice", "Bullet Speed", 4, "rare", "Greatly Increases Bullet Speed"),
    Upgrade("Max Propulsion", "Bullet Speed", 6, "epic", "Massively Increases Bullet Speed"),
    Upgrade("Speed of Light", "Bullet Speed", 10, "pakistinian", "Bullets go the speed of light"),
    Upgrade("Smarts", "Knowledge", 1, "common", "Increases XP per kill by 1"),
    Upgrade("Intelligent", "Knowledge", 2, "rare", "Increases XP per kill by 2"),
    Upgrade("Genius", "Knowledge", 3, "epic", "Increases XP per kill by 3"),
    Upgrade("Infinite Wisdom", "Knowledge", 5, "pakistinian", "Increases XP per kill by 5"),
]

potUpgrades = []

# Converts the rarity of 
for i in potUpgradesRaw:
    match i.rarity:
        case "common":
            for j in range(10): potUpgrades.append(i)
        case "rare":
            for j in range(5): potUpgrades.append(i)
        case "epic":
            for j in range(3): potUpgrades.append(i)
        case "pakistinian":
            for j in range(1): potUpgrades.append(i)

# Screen Parameters
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (6, 69, 23)
BROWN = (82, 49, 2)
PLAYER_COLOR = (242, 177, 97)
SKY_BLUE = (2, 78, 122)
YELLOW = (194, 177, 27)
WHITE = (255, 255, 255)
GREY = (79, 79, 79)
XP_GREEN = (0, 255, 38)
BLUE = (7, 0, 112)
PURPLE = (143, 0, 214)

# Pygame Setup
running = True
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = py.time.Clock()
py.display.set_caption("Pakistan's Bombastic Rougelike")

# Player
playerX = SCREEN_WIDTH / 2
playerY = SCREEN_HEIGHT / 2
playerSpeed = 4

# Gun Reloading
reloading = False
reloadClock = 0
reloadTime = 15

# Bullets
bullets = []
bulletColliders = []
bulletSpeed = 10

# Enemies
regfoes = []
regColliders = []
regSpawnClock = 0
regSpawnTime = 20
regFoeSpeed = 2

# Health
maxHealth = 3
health = 3

# XP
xp = 0
upgradeReq = 10
knowledge = 1 
xp_bar_lengnth = 500
xp_bar_start = 25

# Text
font = py.font.Font(None, 36)
bigFont = py.font.Font(None, 72)

def getColor(rarity): # Returns a color based on rarity (for upgrade cards)
    match rarity:
        case "common": return GREY
        case "rare": return BLUE
        case "epic": return PURPLE
        case "pakistinian": return YELLOW

def get_foe_pos(): # For spawning enemies; spawns an enemy outside of the screen
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
 
    out = []
 
    spawnOption = ["above", "below"] 
    option = choice(spawnOption)
 
    if option == "above":
        out.append(-150)
    else:
        out.append(SCREEN_WIDTH + 150)

    option = choice(spawnOption)

    out.append(randint(-150, SCREEN_HEIGHT + 150))

    return out

def LevelUpOptions(playerSpeed, playerHealth, maxHealth, bulletReload, knowledge, bulletSpeed): # Runs all logic for upgrading the player
    global potUpgrades

    def applyUpgrade(playerSpeed, playerHealth, maxHealth, bulletReload, bulletSpeed, knowledge, stat, amount): # Actually applies the upgrades
        match stat:
            case "Max Health":
                maxHealth += amount
                playerHealth += amount
            case "Player Speed":
                playerSpeed += amount
            case "Reload Time":
                bulletReload *= amount
            case "Full Heal":
                playerHealth = maxHealth
            case "Bullet Speed":
                bulletSpeed += amount
            case "Knowledge":
                knowledge += amount

        return playerSpeed, playerHealth, maxHealth, bulletReload, bulletSpeed, knowledge

    # Setup
    upgrades = []
    rects = []
    for i in range(3): 
        upgrades.append(choice(potUpgrades))
        rect = py.Rect(i * (SCREEN_WIDTH / 3) + 12, 100, (SCREEN_WIDTH / 3) - 25, SCREEN_HEIGHT - 200)
        rects.append(rect)

    while True:
        # Title Text 
        screen.fill(WHITE)
        texty = bigFont.render("Choose An Upgrade!", True, BLACK)
        screen.blit(texty, (25, 25, SCREEN_WIDTH - 50, 50))
        
        # Draws the upgrade boxes
        for i in range(3):   
            color = getColor(upgrades[i].rarity)
            py.draw.rect(screen, color, rects[i])

            text_surface = font.render(upgrades[i].name, True, WHITE)
            screen.blit(text_surface, (i * (SCREEN_WIDTH / 3) + 25, 200, (SCREEN_WIDTH / 3) - 75, 100))

            text_surface_two = font.render(upgrades[i].description, True, WHITE)
            screen.blit(text_surface_two, (i * (SCREEN_WIDTH / 3) + 25, 300, (SCREEN_WIDTH / 3) - 75, 100))

        # Checks to see if any of the boxes have been selected
        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                if rects[0].collidepoint(event.pos):
                    return applyUpgrade(playerSpeed, playerHealth, maxHealth, bulletReload, bulletSpeed, knowledge, upgrades[0].stat, upgrades[0].amount)
                elif rects[1].collidepoint(event.pos):
                    return applyUpgrade(playerSpeed, playerHealth, maxHealth, bulletReload, bulletSpeed, knowledge, upgrades[1].stat, upgrades[1].amount)
                elif rects[2].collidepoint(event.pos):
                    return applyUpgrade(playerSpeed, playerHealth, maxHealth, bulletReload, bulletSpeed, knowledge, upgrades[2].stat, upgrades[2].amount)

        py.display.flip()
            

while running:
    clock.tick(60)

    for event in py.event.get():
            if event.type == py.QUIT:
                running = False 

    keys = py.key.get_pressed()
    screen.fill(SKY_BLUE)

    # Player movement
    if keys[py.K_a]:
        playerX -= playerSpeed
    if keys[py.K_d]:
        playerX += playerSpeed
    if keys[py.K_w]:
        playerY -= playerSpeed
    if keys[py.K_s]:
        playerY += playerSpeed

    # Prevents the player from going out of bounds
    if playerX < 0: playerX = 0
    if playerX > SCREEN_WIDTH: playerX = SCREEN_WIDTH
    if playerY < 0: playerY = 0
    if playerY > SCREEN_HEIGHT: playerY = SCREEN_HEIGHT

    #Bullet firing
    player_pos = py.math.Vector2(playerX, playerY)
    mouse_pos = py.math.Vector2(py.mouse.get_pos())
    direction = mouse_pos - player_pos
    direction = direction.normalize() * bulletSpeed   
    
    if keys[py.K_SPACE] and not reloading:
        bullets.append([playerX + 50, playerY + 50, direction.x, direction.y])
        reloading = True
        reloadClock = 0

    # Fire cooldown
    if reloading:
        reloadClock += 1
        if reloadClock >= reloadTime:
            reloading = False

    # Bullet movement
    fullnew = []
    bulletColliders = []
    for i in bullets:
        new = [round(i[0] + i[2]), round(i[1] + i[3]), i[2], i[3]]
        py.draw.ellipse(screen, BLACK, (new[0], new[1], 20, 20))   
        fullnew.append(new)
        bulletColliders.append(py.Rect(
                    new[0],
                    new[1],
                    50,
                    50
                ))

    bullets = fullnew

    # Enemy spawning
    regSpawnClock += 1
    if regSpawnClock >= regSpawnTime:
        regfoes.append(get_foe_pos())
        regSpawnClock = 0 
 
    fullnew = [] 
    regColliders = [] 
 
    # Enemy movement 
    for i in regfoes: 
        new = i 
        if playerX < i[0]: 
            new[0] -= regFoeSpeed 
        elif playerX > i[0]: 
            new[0] += regFoeSpeed 
        if playerY < i[1]: 
            new[1] -= regFoeSpeed 
        elif playerY > i[1]: 
            new[1] += regFoeSpeed 
 
        fullnew.append(new) 
 
        py.draw.ellipse(screen, BLACK, (new[0], new[1], 50, 50))  

        regfoes = fullnew
        regColliders.append(py.Rect(
                    new[0],
                    new[1],
                    50,
                    50
                ))

    # Checks for bullet-enemy collisions
    for i in bulletColliders:
        for j in regColliders:
            if j.colliderect(i):
                enemy = j
                proj = i
                if [enemy.x, enemy.y] in regfoes: regfoes.remove([enemy.x, enemy.y])

                for k in bullets:
                    if k[0] == proj.x and k[1] == proj.y:
                        bullets.remove(k)

                xp += knowledge
    # Draws the healthbar
    for i in range(maxHealth):
        if i + 1 > health:
            py.draw.ellipse(screen, GREY, (25 + (i * 37), 25, 25, 25))
        else:
            py.draw.ellipse(screen, RED, (25 + (i * 37), 25, 25, 25))

    playerCollider = py.Rect(playerX, playerY, 100, 100)

    # Checks for player-enemy collisions
    for i in regColliders:
        if i.colliderect(playerCollider):
            health -= 1
            if [enemy.x, enemy.y] in regfoes: regfoes.remove([i[0], i[1]])

    # Draws the XP bar
    for i in range(upgradeReq):
        if i + 1 > xp:
            py.draw.rect(screen, GREY, (xp_bar_start + (i * (xp_bar_lengnth / upgradeReq)), 75, (xp_bar_lengnth / upgradeReq), 25))
        else:
            py.draw.rect(screen, XP_GREEN, (xp_bar_start + (i * (xp_bar_lengnth / upgradeReq)), 75, (xp_bar_lengnth / upgradeReq), 25))

    # Upgrade Logic
    if xp >= upgradeReq:
        xp = 0
        upgradeReq = round(upgradeReq * 1.25)
        playerSpeed, health, maxHealth, reloadTime, bulletSpeed, knowledge = LevelUpOptions(playerSpeed, health, maxHealth, reloadTime, bulletSpeed, knowledge)

    # kills the player
    if health <= 0:
        running = False

    py.draw.ellipse(screen, WHITE, (playerX, playerY, 100, 100))
    if running: py.display.flip()