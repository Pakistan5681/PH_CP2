
import pakistans_functions as pf
import csv

def startMenu():
    print("1. View")
    print("2. Add")
    print("3. Remove")
    print("4. Search")
    print("5. Exit")
    print(" ")

    option = pf.idiot_proof_num_range("Choose the number of the option: ", 1, 5)

    if option == 1: view()
    elif option == 2: add()
    elif option == 3: remove()
    elif option == 4: search()
    else: return False

    return True

def add():
    name = input("Whats the title of the book? ").strip()
    author = input("Who is the author of the book ").strip()
    genre = input("What is the genre of the book ").strip()
    year = pf.idiot_proof_general("What year was it published? ")

    with open("Practices/books.csv", "a", newline='') as file:
        outList = [name, author, genre, year]
        writer = csv.writer(file)
        writer.writerow(outList)

def view():
    with open("Practices/books.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} by {row[1]}, a {row[2]} novel written in {row[3]}")

def remove():
    rowsToKeep = []
    with open("Practices/books.csv", "r") as file:
        removeFilter = 0
        filterInput = ""
        view()
        print(" ")
        removeFilter = pf.idiot_proof_specific("Would you like to sort by 'name', 'author', 'genre', or 'year'? ", ["name", "author", "genre", "year"])

        match removeFilter:
            case "name": 
                removeFilter = 0
                filterInput = input("What is the name of the book? ")                
            case "author": 
                removeFilter = 1
                filterInput = input("What is the name of the author? ")
            case "genre": 
                removeFilter = 2
                filterInput = input("What is the books genre? ")
            case "year": 
                removeFilter = 3
                filterInput = input("What year was the book written? ")
            

        reader = csv.reader(file)
        for row in reader: 
            if row[removeFilter] != filterInput:
                rowsToKeep.append(row)

    with open("Practices/books.csv", mode='w', newline='') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(rowsToKeep)

def search():
    with open("Practices/books.csv", "r") as file: 
        removeFilter = pf.idiot_proof_specific("Would you like to sewarch by 'name', 'author', 'genre', or 'year'? ", ["name", "author", "genre", "year"])
        removeFilter = 0
        filterInput = ""

        match removeFilter:
            case "name": 
                removeFilter = 0
                filterInput = input("What is the name of the book? ")                
            case "author": 
                removeFilter = 1
                filterInput = input("What is the name of the author? ")
            case "genre": 
                removeFilter = 2
                filterInput = input("What is the books genre? ")
            case "year": 
                removeFilter = 3
                filterInput = input("What year was the book written? ")

        reader = csv.reader(file)
        for row in reader: 
            if row[removeFilter] == filterInput:
                print(f"{row[0]} by {row[1]}, a {row[2]} novel written in {row[3]}")
                

while True:
    boolean = startMenu()

    if not boolean:
        break
