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
    with open("Practices\\Movies list - Sheet1 (1).csv", "r") as file:
        reader = csv.reader(file)

        print("1. Genre")
        print("2. Director")
        print("3. Actor")
        print("4. Length")

        search_method = input("Choose your filters")
        filters_raw = search_method.split(",")
        filters = {}

        if "1" in filters: 
            filters.append(1)


        if "2" in filters: filters.append(2)
        if "3" in filters: filters.append(3)
        if "4" in filters: filters.append(4)

        for row in reader:
            print(row[1])



def print_list():
    with open("Practices\\Movies list - Sheet1 (1).csv", "r") as file:
        reader = csv.reader(file)
        for line in file:
            print(line)
            sleep(0.025)

        cont = input("Hit enter to continue")
            
menu()