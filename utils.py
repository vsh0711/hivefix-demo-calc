def format_price(amount):
    """Return amount formatted as a dollar string with 2 decimal places, e.g. '$9.50'."""
    return f"${amount:.2f}"


def unique_items(items):
    """Return the items with duplicates removed, preserving first-seen order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def safe_divide(a, b):
    """Return a / b, or None if b is zero (instead of raising)."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def all_positive(numbers):
    """Return True if every number in the list is positive."""
    return all(n > 0 for n in numbers)


def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    return sum(numbers) // len(numbers)
