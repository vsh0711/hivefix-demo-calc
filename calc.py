def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference a - b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def is_positive(n):
    """Return True if n is strictly greater than zero."""
    return n > 0


def factorial(n):
    """Return n! (the factorial of n)."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def divide(a, b):
    """Return a divided by b."""
    return a / b


def max_of(a, b):
    """Return the larger of a and b."""
    if a > b:
        return a
    return b


def remainder(a, b):
    """Return the remainder of a divided by b."""
    return a % b
