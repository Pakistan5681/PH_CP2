class Monke:
    def __init__(self, name, age, race):
        self.name = name.title()
        self.age = age
        self.race = race.title()

    def __str__(self):
        return f"{self.name} is a {self.race} who is {self.age} years old"
    
print(Monke("The arch monke", "unknown", "Shattered Fragment of Omnum"))
print(Monke("Chaos Lord", 27492031, "Chaos Elemental"))
print(Monke("The Weeping Executioner", 54, "Trueborn [corrupted]"))
print(Monke("Keyon", 24, "Canisborn"))
print(Monke("Urk", 44, "Ursusborn"))
print(Monke("Sylvania", 52, "Felisborn"))
print(Monke("the player", 22, "trueborn"))