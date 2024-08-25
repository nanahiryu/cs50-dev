import csv

houses = {"Gryffindor": 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin": 0}

with open("Hogwarts.csv", "r") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        # house = row[1]
        house = row["House"]
        houses[house] += 1

print(houses)
