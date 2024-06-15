#Crear una prueba pytest por categorías para el archivo calculator.py

from calculator import square
import pytest

#Positive test
def test4_positive():
    assert square(2) == 4
    assert square(3) == 9

#Negative test
def test4_negative():
    assert square(-2) == 4
    assert square(-3) == 9

#Zero test
def test4_zero():
    assert(0) == 0


#Agregar una función que tambíen indique errores en cadenas str
def test4_str():
    with pytest.raises(TypeError):
        square("cat")

