import pytest

from mylib.calc import add, subtract, multiply, divide, power, square_root, absolute, is_even, is_odd


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-4, -2) == -2


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 99) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-12, 3) == -4
    assert divide(7, 2) == 3.5

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 1) == 3
    assert power(2, -2) == 0.25


def test_square_root():
    assert square_root(16) == 4
    assert square_root(0) == 0
    assert square_root(25) == 5

    with pytest.raises(ValueError):
        square_root(-1)


def test_absolute():
    assert absolute(-5) == 5
    assert absolute(5) == 5
    assert absolute(0) == 0


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True


def test_is_odd():
    assert is_odd(2) is False
    assert is_odd(3) is True
    assert is_odd(0) is False
    assert is_odd(-5) is True
