name = input("¿Cuál es su nombre?")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

