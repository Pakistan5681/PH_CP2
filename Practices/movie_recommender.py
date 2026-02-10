import pakistans_functions as pf
from time import sleep
import csv

def menu():
    while True:
        print("1. Search movie or get recommendation")
        print("2. Print movie list")
        print("3. Quit")
        print(" ")

        option = pf.idiot_proof_num_range("Enter the number of the option ", 1, 3)

        match option:
            case 1:
                search_or_recommend()
            case 2:
                print_list()
            case 3:
                break


def search_or_recommend():
    with open("Practices/Movies list - Sheet1 (1).csv", "r") as file:
        reader = list(csv.reader(file))

        print("1. Genre")
        print("2. Director")
        print("3. Actor")
        print("4. Length")

        search_method = input("Choose your filters ")
        filters_raw = search_method.split(",")
        filters = {}

        if "1" in filters_raw: 
            genreToAdd = input("What genre do you want to sort by? ")
            filters[1] = genreToAdd.strip().capitalize()

        if "2" in filters_raw:
            director = input("What director do you want to sort by? ")
            filters[2] = director.strip().capitalize()

        if "3" in filters_raw:
            actor = input("What actor do you want to sort by? ")
            filters[3] = actor.strip().capitalize()
        
        if "4" in filters_raw:
            legnthMin = pf.idiot_proof_general("What is the shortest time (in minutes) the movie can be ")
            legnthMax = pf.idiot_proof_general("What is the longest time (in minutes) the movie can be ")
            filters[4] = (legnthMin, legnthMax)

        potentail_films = []
        for row in reader:
            potentail_films.append(", ".join(row))

        

        if 1 in filters.keys():
            for row in reader:
                if  "/" in row[2]: genres = row[2].split("/")
                else: genres= row[2]

                print(row[2])

                if not row[2] in genres:
                    genres = row
                    potentail_films.remove(", ".join(row))

        for i in potentail_films:
            print(i)
            



def print_list():
    with open("Practices\\Movies list - Sheet1 (1).csv", "r") as file:
        reader = csv.reader(file)
        for line in file:
            print(line)
            sleep(0.025)

        cont = input("Hit enter to continue")
            
menu()