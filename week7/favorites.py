import csv

with open("Hogwarts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["House"])
