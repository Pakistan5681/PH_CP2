
import csv
with open("Random Files\\beans.csv", "r", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for lines in csvfile:
        print(lines)
    