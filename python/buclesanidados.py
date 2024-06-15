#Ejemplo 1 bucles aninados
def main():
    print("Estamos en la linea3 probando los bucles anidados, impresion de columna, ejemplo 1")
    print_column(3)

def print_column(height):
    """for _ in range(height):
        print("$")"""
    print("#\n" * height, end="")
main()
print()


#Ejemplo 2 bucles anidados
def row():
    print("Estamos en la linea14 probanodo los bucles anidados, impresión en línea, ejemplo 2")
    print_row(4)

def print_row(width):
    print("?" * width)
row()
print()


#Ejemplo 3 buclea anidados
def square():
    print("Estamos en la linea27 probando los bucles anidados, imprimiendo columnas y filas, ejemplo 3")
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

square()
print()


#Ejemplo 4 bucles anidados
def sqr():
    print("Estanos en la linea42 probando los bucles anidados, impresion de filas y columnas, ejemplo 4")
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

sqr()
print()
