def format_price(amount):
    """Return amount formatted as a dollar string with 2 decimal places, e.g. '$9.50'."""
    return f"${amount:.2f}"


def unique_items(items):
    """Return the items with duplicates removed, preserving first-seen order."""
    return list(set(items))


def safe_divide(a, b):
    """Return a / b, or None if b is zero (instead of raising)."""
    try:
        return a / b
    except TypeError:
        return None


def all_positive(numbers):
    """Return True if every number in the list is positive."""
    return any(n > 0 for n in numbers)
