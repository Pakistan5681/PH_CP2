import pakistans_functions as pf

books = []

nameRef = {}
authorRef = {}

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

    outString = f"{name} by {author}"
    print(outString)
    books.append(outString)

    nameRef[name] = outString
    if author in authorRef.keys(): authorRef[author].append(outString)
    else: 
        authorRef[author] = []
        authorRef[author].append(outString)

def view(): 
    if bool(books):
        print(" ")  
        for i in books: print(i)    
        print(" ")
    else:
        print("You have no books in your library")

def remove():
    if bool(books):
        removeFilter = pf.idiot_proof_specific("Would you like to sort by 'name' or 'author'? ", ["name", "author"])

        view()
        print(" ")
        if removeFilter == "author":
            authors = []
            for i in authorRef.keys(): authors.append(i)

            author = pf.idiot_proof_specific("What is the name of the author? ", authors, "That author has not written any books in your library")

            for i in authorRef[author]:
                books.remove(i)
                print(f"{i} was removed from your library")

            del authorRef[author]
        else:
            names = []
            for i in nameRef.keys(): names.append(i)

            name = pf.idiot_proof_specific("What is the name of the book? ", names, "That book is not in your library")
            books.remove(nameRef[name])
            print(f"{nameRef[name]} was removed from your library")

            del nameRef[name]
    else:
        print("You have no books in your library")

def search():
    if bool(books):
        authors = []
        for i in authorRef.keys(): authors.append(i)

        author = pf.idiot_proof_specific("What author do you want to look up? ", authors, "That author has not written any books in your library")
        print(" ")

        for i in authorRef[author]:
            print(f"You have {i} in your library")
    else:
        print("You have no books in your library")


while True:
    boolean = startMenu()

    if not boolean:
        break