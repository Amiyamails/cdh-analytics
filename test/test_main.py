import pytest
from config.MathOperations import MathOperations

math_ops = MathOperations()

def test_add():
    assert math_ops.add(2, 3) == 5

def test_subtract():
    assert math_ops.subtract(5, 3) == 2

def test_multiply():
    assert math_ops.multiply(4, 3) == 12
