from utils import all_positive, format_price, safe_divide, unique_items


def test_format_price():
    assert format_price(9.5) == "$9.50"


def test_unique_items_preserves_order():
    assert unique_items([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_safe_divide_zero():
    assert safe_divide(5, 0) is None


def test_all_positive_rejects_one_negative():
    assert all_positive([1, 2, -3, 4]) is False
