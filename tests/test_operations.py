import pytest

from calculator import add, divide


def test_add_sums_two_numbers():
    assert add(2, 3) == 5


def test_divide_divides_two_numbers():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(1, 0)
