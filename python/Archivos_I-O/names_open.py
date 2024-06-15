name = input("¿Cuál es su nombre?")

file = open("names.txt", "w")
file.write(name)
file.close()

