#Creación de la función hello para prueba de coleccion en una carpeta

def main():
    name = input("¿Cuál es sun nombre? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()

