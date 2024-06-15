# Ejemplo 1, Manejo de errores con try, excepciones.
print("Estamos en la línea2 probando try")
try:
    x = int(input("¿Cuánto es x? "))
except ValueError:
    print("x no equivale a un entero")

# print(f"x es {x}")

else: # se puede usar else si no se detecta error en la excepción.
    print(f"x es {x}")
print()

# Ejemplo 2, Manejo de try con bucle while True. break.
print("Estamos en la línea15 probando try con el bucle while True")
while True:
    try:
        a = int(input("¿Cuánto es a? "))
    except ValueError:
        print("a no equivale a un entero")

# print(f"x es {x}")

    else: # se puede usar else si no se detecta error en la excepción
        break # se usa un break para salir del bloque while
print(f"a es {a}")
print()

# Ejemplo 3, manejo de errores y retorno de valores con función get_int
print("Revisar código en línea30 para ejemplo 3 de uso de función get_int para try")
"""
def get_int():
    while True:
        try:
            b = int(input("¿Cuanto es b?"))
        except ValueError:
            print("b no es un entero")
# print(f"x es {x}")
        else:
            break
        return b
get_int()
"""
print()
# Ejemplo 3 simplificado
print("Estamos en la línea46 probando la simplificación de la función get_int para el uso de try")
def main():
    c = get_int()
    print(f"c es {c}")


def get_int():
    while True:
        try:
            return int(input("¿Cuanto es c?"))
        except ValueError:
            print("c no equivale a un entero")


main()
print()
# Ejemplo 4, uso de pass para pasar por alto un error.
print("Estamos en la línea63 probanod pass para ignorar errores")
def ign_error():
    d = ign_pass()
    print(f"d es {d}")


def ign_pass():
    while True:
        try:
            return int(input("Cuánto es d? "))
        except ValueError:
            pass


ign_error()
print()
#Ejemplo 5, argumentos de funciones con parámetros "prompt"
print("Estamos en la línea80 probando el parámetro prompt en la función")
def arg_prmt():
    e = ign_prmt("¿Cuánto es e? ")
    print(f"e es {e}")


def ign_prmt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


arg_prmt()
print()

