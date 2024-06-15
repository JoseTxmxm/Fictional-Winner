# Ciclo while
print("Estamos en la linea 2 probando el ciclo while, imprimir meow 3 veces")
a = 3

while a != 0:
    print("meow")
    a = a - 1
print("")

# Ciclo while2
print("Estamos en la linea 12 probando el ciclo while, imprimir meow 3 veces")
b = 0
while b < 3:
    print("meow")
    b += 1
print("")

#Ciclos for
print("Estamos en la linea 19 probando el ciclo for, imprimir meow 3 veces")
for c in [0, 1, 2]:
    print("meow")
print("")

#Ciclo for 2
print("Estamso en la linea 25 probando el ciclo for, imprimir meow 3 veces")
for d in range(3):
    print("meow")
print("")
print("Estamos en la linea 29 simplificando los ciclos anteriores, impirmir meow 5 veces en una sola linea")
print("meow\n" * 5, end="")
print("")

#Validacion de entradas
print("Estamos en la linea 34 probando la validacion de entradas con los ciclos while, for y condicional if")
while True:
    n = int(input("Cuanto es n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
print("")

#Validacion de entradas con funcion
print("Estamos en la linea 45 probando la validacion de entradas con la llamada a una funcion")
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        m = int(input("Cuanto es n? "))
        if m > 0:
            break
    return m

def meow(m):
    for _ in range(5):
        print("meow")
main()
#Iteracion con listas
students = ["Hermion", "Harry", "Tomy"]

print(students)
print("linea 5, impimir cada estudiante individualemente")
print(students[0])
print(students[1])
print(students[2])
print()
print("linea 10, for student in students")
for student in students:
    print(student)
print()
#imprimir listas con ls funcion len
print("linea 14, Imprimir lista students con la funcion len, i + 1")
for i in range(len(students)):
    print(i + 1, students[i])

print()
#Diccionario, claves y valores
print("Estamos en la linea81 probando la impresion de claves y valores de un diccionario")
students2 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student2 in students2:
    print(student2, students2[student2], sep=", ")
print()
#Lista de diccionarios
print("Estamos en la linea91 probando la impresion de una lista en el diccionario")
students3 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stage"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for student3 in students3:
    print(student3["name"], student3["house"], student3["patronus"], sep=", ")
print()

