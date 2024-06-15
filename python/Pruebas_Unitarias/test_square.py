#Importar la función square para crear la función test_square

from calculator import square

def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared no era 4")

    if square(3) != 9:
        print("3 squared no era 9")


if __name__ == "__main__":
    main()

