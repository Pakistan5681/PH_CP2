import pakistans_functions as pf

books = []

def startMenu():
    print("1. View")
    print("2. Add")
    print("3. Remove")
    print("4. Search")
    print("5. Exit")
    print(" ")

    option = pf.idiot_proof_num_range("Choose the number of the option: ", 1, 5)

    if option == 1:
        add()

def add():
    name = input("Whats the title of the book? ").strip()
    author = input("Who is the author of the book").strip()

    print(f"Added {name} by {author}")
    books.append(f"{name} by {author}")
