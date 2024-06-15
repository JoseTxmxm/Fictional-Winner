#Crear una prueba de colección de errores para la función de hello.py

from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Jose") == "hello, Jose"

