from random import choice, randint
import pakistans_functions as pf

def main():
    while True:
        get_input_for_password()
        continueProgram = pf.idiot_proof_yes_no("Would you like to continue using the program ")

        if not continueProgram:
            print("Exiting program")
            break

def get_input_for_password():
    length = pf.idiot_proof_general("How many characters do you want in your password ")
    includeLower = pf.idiot_proof_yes_no("Require lowercase? ")
    includeUpper = pf.idiot_proof_yes_no("Require uppercase? ")
    includeNumber = pf.idiot_proof_yes_no("Require number? ")
    includeSpecial = pf.idiot_proof_yes_no("Require special character? ")

    print("Possibilites:")
    print(" ")
    for i in range(4):
        print(generate_password(length, includeLower, includeUpper, includeNumber, includeSpecial))
        print(" ")

def generate_password(length, needs_lowercase, needs_uppercase, needs_number, needs_spec_chars): #actually generates the code
    possibilites = []
    password = ""
    removeAmount = 0 # used to make sure the right amount of default characters are added to possibilites

    if needs_lowercase: removeAmount += 1
    if needs_uppercase: removeAmount += 1
    if needs_number: removeAmount += 1
    if needs_spec_chars: removeAmount += 1

    for i in range(length - removeAmount): possibilites.append("reg") # removes a default character for every specific character added
    if needs_lowercase: possibilites.append("lower")
    if needs_uppercase: possibilites.append("upper")
    if needs_number: possibilites.append("num")
    if needs_spec_chars: possibilites.append("spec")

    for i in range(length):
        char = choice(possibilites)

        if char == "reg": 
            password += generate_standard_character()
            possibilites.remove("reg")
        elif char == "lower":
            password += generate_lowercase()
            possibilites.remove("lower")
        elif char == "upper":
            password += generate_uppercase()
            possibilites.remove("upper")
        elif char == "num":
            password += generate_number()
            possibilites.remove("num")
        elif char == "spec":
            password += generate_special()
            possibilites.remove("spec")
        else:
            password += generate_standard_character()

    return password
            

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
    char_code = randint(35, 47)
    return chr(char_code)

main()