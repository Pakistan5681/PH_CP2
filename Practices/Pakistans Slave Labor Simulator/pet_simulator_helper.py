from time import sleep

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

    def get_mood(self):
        if self.happiness > 80:
            return "happy"
        elif self.happiness > 60:
            return "mediorcre"
        elif self.happiness > 40:
            return "sad"
        elif self.happiness > 20:
            return "depressed"
        else:
            return "extremely depressed"
        
    def get_health(self):
        if self.health > 80:
            return "healthy"
        elif self.health > 60:
            return "fine"
        elif self.health > 40:
            return "unhealthy"
        elif self.health > 20:
            return "sickly"
        else:
            return "near death"
        
    def get_hunger(self):
        if self.hunger > 80:
            return "full"
        elif self.hunger > 60:
            return "satified"
        elif self.hunger > 40:
            return "hungry"
        elif self.hunger > 20:
            return "ravenous"
        else:
            return "starving"
        
    def get_thirst(self):
        if self.thirst > 80:
            return "fully hydrated"
        elif self.thirst > 60:
            return "mostly hydrated"
        elif self.thirst > 40:
            return "parched"
        elif self.thirst > 20:
            return "bone-dry"
        else:
            return "entirely dehydrated"
    
    def get_energy(self):
        if self.thirst > 80:
            return "energetic"
        elif self.thirst > 60:
            return "awake"
        elif self.thirst > 40:
            return "tired"
        elif self.thirst > 20:
            return "exahsted"
        else:
            return "practically asleep"
        
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
        
    def day(self):
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
            case "default":
                self.hunger += 50
            case "super":
                self.hunger = 100
                self.energy += 50
            case "wet":
                self.hunger += 50
                self.thirst += 50
            case "medicinal":
                self.hunger += 50
                self.health += 25
            case "tasty":
                self.hunger += 50
                self.happiness += 25

        self.normalize_vars()

    def water(self):
        self.thirst += 50
        if self.thirst > 100: self.thirst = 100

    def send_to_bed(self):
        self.awake = False
        self.energy = 100

    def play(self, total_fun):
        self.happiness += total_fun
        self.hunger -= 5
        self.thirst -= 5
        self.normalize_vars()
        
    def __str__(self):
        if self.alive:
            if self.awake:
                return f"{self.name} is {self.age} years old. Mood: {self.get_mood()}. Hunger: {self.get_hunger()}. Thirst: {self.get_thirst()}.\nHealth: {self.get_health()}. Energy: {self.get_energy()}"
            else:
                return f"{self.name} is sleeping."
        else:
            return f"{self.name} died at age {self.age}"

pets = []

def menu():
    if bool(pets):
        day
    else:
        start()

def day():
    pass

def start():
    print("Welcome to Pakistans Slave Labor Simulator")
    sleep(1)
    print(" ")
    print("I mean, welcome to Pakistans Pet Simulator")
    sleep(0.5)
    print("Of course")
    print()