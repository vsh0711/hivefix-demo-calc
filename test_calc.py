from calc import add, factorial, is_positive, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_is_positive_zero_is_not_positive():
    assert is_positive(0) is False


def test_is_positive_positive_number():
    assert is_positive(5) is True


def test_factorial():
    assert factorial(5) == 120
