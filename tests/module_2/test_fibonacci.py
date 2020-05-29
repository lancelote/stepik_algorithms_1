import pytest

from module_2.fibonacci import fibonacci


@pytest.mark.parametrize("n,expected", [(1, 1), (2, 1), (3, 2), (8, 21),])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected
