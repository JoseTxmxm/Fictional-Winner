#Creación de segunda prueba para el archivo calculator.py

from calculator import square


def main():
    test_square2()


def test_square2():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared no era 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared no era 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared no era 0")


if __name__ == "__main__":
    main()




