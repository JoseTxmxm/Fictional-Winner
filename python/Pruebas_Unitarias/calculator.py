#Crear una calculadora que calcule el cuadrado de un número.

def main():
    x = int(input("¿Cuánto es x? "))
    print("x squared es: ", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
