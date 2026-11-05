from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_subtract():
    assert subtract(6, 4) == 2

def test_multiply():
    assert multiply(2, 5) == 10

def test_divide_uneven():
    #arrange
    a, b = 5, 2
    #Act
    result = divide(a, b)
    #Assert
    assert result == 2.5

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5), (-2, -3, -5), (0, 0, 0),
])
def test_add_many(a, b, expected):
    assert add(a, b) == expected
