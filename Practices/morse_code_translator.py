import pakistans_functions as pf

morse = (
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--.."
)

letters = (
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z"
)

message = "hello"

def translate_to_letter(message, morse, letters):
    allSymbols = message.split()
    outMessage = ""

    for i in allSymbols:
        if i in morse:
            outMessage += letters[morse.index(i)]

    print(outMessage)

def translate_to_morse(message, morse, letters):
    outMessage = ""

    for i in message:
        if i in letters:
            outMessage += morse[letters.index(i)]

    print(outMessage)

def main_loop(morse, letters):
    """
    Runs the inputted function then asks the user if they would like to continue with the program
    """

    while True:
        print("1. Morse code to english\n2. English to morse code")
        option = pf.idiot_proof_num_range("Enter the number of the desired option ", 1, 2)
        
        message = input("Input the message you would like to translate ")

        if option == 1: translate_to_letter(message, morse, letters)
        else: translate_to_morse(message, morse, letters)
        
        continueProgram = pf.idiot_proof_yes_no("Would you like to continue using the program ")

        if not continueProgram: 
            break

main_loop(morse, letters)