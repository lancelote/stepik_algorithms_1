import pytest

from module_4.continuous_backpack import max_value, Thing


@pytest.mark.parametrize('capacity,things,expected', [
    (50, [Thing(60, 20), Thing(100, 50), Thing(120, 30)], 180),
])
def test_max_value(capacity, things, expected):
    assert max_value(capacity, things) == expected
