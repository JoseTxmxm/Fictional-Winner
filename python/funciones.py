# Inicialización de funciones en python
print("defininedo funciones, ejemplo 1")


def main():
    name = input("what's your name? ")
    print(name)

    def hello(to="world,"):  # La función no se ejcutará dentro de main
        print("hello,", to)


main()

print("Ejemplo 2")


def hello(to="world,"):
    print("hello,", to)


hello()
print("")

print("Ejemplo 3, scope")


def put():
    last_name = input("Escriba su apellido: ")
    nom(last_name)


def nom(x):
    print("Good-Bye", x)


put()
print("")

print("Ejemplo 4, calculadora")


def main():
    x = int(input("Valor de x: "))
    print("x squared is:", squared(x))


def squared(n):
    return n * n


main()
print("")
