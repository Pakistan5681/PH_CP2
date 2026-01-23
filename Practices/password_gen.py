from random import choice, randint
import pakistans_functions as pf

def generate_password(length, needs_lowercase, needs_uppercase, needs_number, needs_spec_chars): #actually generates the code
    possibilites = []
    password = ""

    for i in range(length - 4): possibilites.append("reg")
    if needs_lowercase: possibilites.append("lower")
    if needs_uppercase: possibilites.append("upper")
    if needs_number: possibilites.append("num")
    if needs_spec_chars: possibilites.append("spec")

    for i in range(length):
        char = choice(possibilites)

        if char == "reg": password += generate_standard_character()

def generate_standard_character():  # generates a random character using ascii
    char_code = randint(35, 126)
    return chr(char_code)

def generate_number(): # generates a random number using ascii
    char_code = randint(48, 57)
    return chr(char_code)

def generate_uppercase(): # generates a random uppercase letter using ascii
    char_code = randint(65, 90)
    return chr(char_code)

def generate_lowercase(): # generates a random lowercase letter using ascii
    char_code = randint(65, 90)
    return chr(char_code)

def generate_special(): # generates a random special character using ascii
    char_code = randint(33, 47)
    return chr(char_code)

for i in range(100):
    print(generate_standard_character())