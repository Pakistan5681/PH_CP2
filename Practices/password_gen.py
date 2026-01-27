from random import choice, randint
import pakistans_functions as pf

asciiNumbers = {
    "reg": [35, 126],
    "lower" : [96, 122],
    "upper" : [65, 90],
    "spec" : [35, 47],
    "num" : [48, 57]          
}

def main():
    while True:
        get_input_for_password()
        continueProgram = pf.idiot_proof_yes_no("Would you like to continue using the program ")

        if not continueProgram:
            print("Exiting program")
            break

def get_input_for_password():
    length = pf.idiot_proof_num_range("How many characters do you want in your password ", 6, 99, "integer", "The length must be more than 5 and less than 100\n ")
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

    if needs_lowercase: removeAmount += 1; possibilites.append("lower")
    if needs_uppercase: removeAmount += 1; possibilites.append("upper")
    if needs_number: removeAmount += 1; possibilites.append("num")
    if needs_spec_chars: removeAmount += 1; possibilites.append("spec")

    for i in range(length - removeAmount): possibilites.append("reg") # removes a default character for every specific character added

    for i in range(length):
        char = choice(possibilites)
        password += generateAscii(asciiNumbers[char][0], asciiNumbers[char][1])

    return password
            
def generateAscii(min, max):
    char_code = randint(min, max)
    return chr(char_code)

main()