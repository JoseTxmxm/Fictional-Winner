import csv

name = input("¿Cuál es tu nombre? ")
home = input("¿Dónde vives? ")

with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])

    writer.writerow({"home": home, "name": name})
