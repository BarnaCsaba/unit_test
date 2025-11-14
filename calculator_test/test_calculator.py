import pytest
from calculator import add, subtract, multiply, divide  

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-2, -3) == -5
    assert sum(-1, 1) == 0   
def test_substract():
    assert substract(5, 3) == 2
    assert substract(0, 0) == 0
    assert substract(-1, -1) == 0   

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    with pytest.raises(ValueError):
        divide(5, 0)