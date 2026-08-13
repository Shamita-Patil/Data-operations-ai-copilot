import pytest


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5


def subtract(a, b):
    return a - b


def test_subtract():
    assert subtract(10, 5) == 5


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)