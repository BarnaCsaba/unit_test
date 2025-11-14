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
