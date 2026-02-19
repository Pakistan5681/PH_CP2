import pakistans_functions as pf
import datetime

path = ""

# !!! There's a file with the path Docs\word_counter_document.txt specifically for writing in !!!

def menu(path):
    while True:
        print("1. Update Document")
        print("2. View Document")
        print("3. Add Content to Document")
        print("4. Exit program")

        print(" ")
        userInput = pf.idiot_proof_num_range("Type the number of the desired option ", 1, 4)        

        match userInput:
            case 1: path = update(path)
            case 2: view(path)
            case 3: add(path)
            case 4: break

def update(path):
    if findFile(path, True):
        print(" ")
        print("Document updated")
        print(f"Word count: {getWordCount()}")
        with open("Docs\\word_counter_time.txt", "r") as file:
            print(f"Last updated {file.read()}")

        return path
    else:
        while True:
            print(" ")
            newPath = input("What is the file path of your document? ")
            if findFile(newPath):
                break

        print("File path updated")
        return newPath


def view(path):
    if findFile(path, False):
        print(" ")
        with open(path, "r") as file:
            print(file.read())
        print(" ")

def add(path):
    if findFile(path, False):
        print(" ")
        with open(path, "a") as file:
            additive = input("What would you like to add to your document? ")
            file.write(" " + additive)

        with open("Docs\\word_counter_time.txt", "w") as file:
            file.write(str(datetime.datetime.now()))

def getWordCount(path):
    if findFile(path, False):
        with open(path, "r") as file:
            wordsRaw = file.read()
            words = wordsRaw.split(" ")

            return len(words)

def findFile(path, updating):
    if path != "":
        try:
            with open(path, "r") as file:
                return True

        except FileNotFoundError:
            print(" ")
            print(f"The file '{path}' does not exist")
            print(" ")
            return False
    else:
        if not updating: 
            print(" ")
            print("You havent selected a file yet. Use the 'Update Document' method to choose a file path")
            print(" ")
        return False


menu(path)        
