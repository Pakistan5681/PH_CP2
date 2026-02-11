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
        
        print(" ")


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
            lengthMax = pf.idiot_proof_general("What is the longest time (in minutes) the movie can be ")
            filters[4] = (legnthMin, lengthMax)

        potentail_films = []

        for row in reader:
            potentail_films.append(", ".join(row))

        if 1 in filters.keys():
            for row in reader:
                if  "/" in row[2]: genres = row[2].split("/")
                else: genres= [row[2]]

                if not genreToAdd in genres:
                    potentail_films.remove(", ".join(row))

        if 2 in filters.keys():
            file.seek(0)
            reader2 = csv.reader(file)
            for row in reader2:
                directors = row[1].split(", ")
                if not director in directors:
                    if ", ".join(row) in potentail_films: potentail_films.remove(", ".join(row))

        if 3 in filters.keys():
            file.seek(0)
            reader3 = csv.reader(file)
            for row in reader3:
                actors = row[5].split(", ")
                if not actor in actors:
                    if ", ".join(row) in potentail_films: potentail_films.remove(", ".join(row))

        if 4 in filters.keys():
            file.seek(0)
            reader4 = csv.reader(file)
            for row in reader4:
                time = row[4]
                if type(time) == int: 
                    validTime = time >= legnthMin and time <= lengthMax
                    if not validTime:
                        if ", ".join(row) in potentail_films: potentail_films.remove(", ".join(row))

        for i in potentail_films:
            print(i)
            sleep(0.02)

        if not bool(potentail_films): print("There are no movies that meet that requirement")

        cont = input("Hit enter to continue")
            



def print_list():
    with open("Practices\\Movies list - Sheet1 (1).csv", "r") as file:
        reader = csv.reader(file)
        for line in file:
            print(line)
            sleep(0.025)

        cont = input("Hit enter to continue")
            
menu()