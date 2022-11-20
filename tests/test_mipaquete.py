import math
import numpy as np
from mipaquete.math import add, subtract, multiply
from mipaquete.string import lowercase, uppercase


# testing mipaquete.math
# add
def test_add():
    """Test adding two integers"""
    assert math.isclose(add(2, 3), np.add(2, 3))


def test_add1():
    """Test adding zero and a negative number"""
    assert math.isclose(add(0, -1), np.add(0, -1))


def test_add2():
    """Test adding a negative number and a float"""
    assert math.isclose(add(-1, 0.99), np.add(-1, 0.99))


# substract
def test_subtract():
    """Test subtracting two integers"""
    assert math.isclose(subtract(2, 5), np.subtract(2, 5))


def test_subtract2():
    """Test subtracting two negative numbers"""
    assert math.isclose(subtract(-150, -25.2), np.subtract(-150, -25.2))


def test_subtract3():
    """Test subtracting two floats"""
    assert math.isclose(subtract(-0.025, 1.236), np.subtract(-0.025, 1.236))


# multiply
def test_multiply():
    """Test multiplying two integers"""
    assert math.isclose(multiply(2, 5), np.multiply(2, 5))


def test_multiply2():
    """Test multiplying two negative numbers"""
    assert math.isclose(multiply(-150, -25.2), np.multiply(-150, -25.2))


def test_multiply3():
    """Test multiplying two floats"""
    assert math.isclose(multiply(-0.025, 1.236), np.multiply(-0.025, 1.236))


# testing mipaquete.string
text = "Texto con el número 21 y una ñ y $$ EN MAYÚSCULA."


def test_lowercase():
    """Test text gets converted to lower case"""
    assert lowercase(text) == text.lower()


def test_uppercase():
    """Test text gets converted to upper case"""
    assert uppercase(text) == text.upper()
