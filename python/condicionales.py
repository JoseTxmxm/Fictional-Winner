# Códigos de prueba python

# Condiconal if
print("Ejemplo 1, condicional if")
x = int(input("Que es x? "))
y = int(input("Que es y? "))

if x > y:
    print("x es mayor que y")
if x < y:
    print("x es menor que y")
if x == y:
    print("x es equivalente a y")
print("")
print("Ejemplo 2 condicionales elif, comentarios en codigo")
"""
# Condicional elif
print("Ejemplo 1, condicional if")
x = int(input("Que es x?"))
y = int(input("Que es y?"))

if x > y:
    print("x es mayor que y")
elif x < y:
    print("x es menor que y")
elif x == y:
    print("x es equivalente a y")
print("")
"""
print("Diferenciar cambios de diagrama de flujo, simplificacion del codigo entre el uso de if, elif")
print("")
print("Ejemplo 3, uso de else, simplificacion de codigo")
a = int(input("Que es a? "))
b = int(input("Que es b? "))

if a > b:
    print(" a es mayor que b")
elif a < b:
    print(" a es menor que b")
else:
    print(" a es equivalente a \"b\"")
    print("")
print("Diferenciar cambios de diagrama de flujo, simplificacion del codigo entre el uso de elif, else")
print("")

# Ejemplo 4, or
print("Ejemplo 4, condicional or")
c = int(input("Que es c? "))
d = int(input("Que es d? "))

if c > d or c < d:
    print(" c no es equivalente a d")
else:
    print(" c es equivalente a d")
print("")

# Ejemplo 5, not equal
print("Ejemplo 5, not equal")
if c != d:
    print(" c is not equal to b ")
else:
    print(" c is equal to b ")
print("")
print("Recordatorio correcta implementacion de indentacion con la sangria")
print("")
# Ejemplo 6, AND
print("Ejemplo 6, condicoinal AND")

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grado A")
elif score >= 80 and score <= 90:
    print("Grado B")
elif score >= 70 and score <= 80:
    print("Grado C")
elif score >= 60 and score <= 70:
    print("Grado D")
else:
    print("Grado F")
print("")

# Ejemplo 7, anidacion y encadenamiento de operadores
print("Línea 85, Ejemplo 7, anidacion y encadenamiento de operadores de Score, comentarios en codigo")
"""
if score 90 >= score <= 100:
    print("Grado A")
elif score 80 >= score < 90:
    print("Grado B")
elif score 70 >= score < 80:
    print("Grado C")
elif score 60 >= score < 70:
    print("Grado D")
else:
    print("Grado F")
print("")
"""
print("")
# Ejemplo 8, optimizacion de operadores
print("Línea 101: Ejemplo 8, optimizacion de operadores ejemplo 7, comentarios en codigo")
"""
if score >= 90:
    print("Grado B")
elif score >= 80:
    print("Grado C")
elif score >= 70:
    print("Grado D")
else:
    print("Grado F")
"""
print("")
print("Precaucion con bugs!")
print("")
# Ejemplo 9, operador modulo
print("Ejemplo 9, implementacion del modulo % para imprimir par o impar")
# Declaracion de la funcion


def main():
    e = int(input("Que es e? "))
    es_par(e)


def es_par(n):
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")


main()
print("")
# Ejemplo 10, expresiones booleanas True, False
print("Ejemplo 10, expresiones booleanas True, False")


def pares():
    f = int(input("Que es f? "))
    if es_par(f):
        print("Es par")
    else:
        print("Es impar")


def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


pares()
print("")
# Ejemplo 11, expresiones pythonicas
print("Ejemplo 11, expresiones pythonicas return True if n % 2 == 0 else return False")


def pytho():
    g = int(input("Que es g? "))
    if n_par(g):
        print("Es par")
    else:
        print("Es impar")


def n_par(n):
    return True if n % 2 == 0 else False


pytho()
print("")
# Ejemplo 12, match
print("Ejemplo 12, match")
print("Nombres: Terry, Melanie, Petersvraus, Hensy")
nombre = input("Ingrese un nombre: ")

match nombre:
    case "Terry":
        print("Es un buen estudiante")
    case "Melanie":
        print("She have a bondle hair")
    case "Petervraus":
        print("El habla italiano")
    case "Hensy":
        print("Ella es muy amable")
    case _:
        print("No se de el, ella")
print("")
