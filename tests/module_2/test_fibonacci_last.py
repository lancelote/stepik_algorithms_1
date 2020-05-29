import pytest

from module_2.fibonacci_last import fib_digit


@pytest.mark.parametrize(
    "n,expected", [(317457, 2), (1, 1), (2, 1), (3, 2), (10, 5),]
)
def test_fib_digit(n, expected):
    assert fib_digit(n) == expected
