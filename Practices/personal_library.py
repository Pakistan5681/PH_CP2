import pakistans_functions as pf

books = []
names = []

nameRef = {} # References books by name
authorRef = {}# References books by author

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

def add():
    name = input("Whats the title of the book? ").strip()
    author = input("Who is the author of the book? ").strip()

    print(f"Added {name} by {author}")
    books.append(f"{name} by {author}")
    names.append(name)

def view():
    if bool(books):
        for i in books:
            print(i)
    else:
        print("There are no books in your personal library")

def remove():

while True:
    boolean = startMenu()

    if not boolean:
       break
