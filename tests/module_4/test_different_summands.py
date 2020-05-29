import pytest

from src.module_4.different_summands import different_summands


@pytest.mark.parametrize("n,summands", [(4, [1, 3]), (6, [1, 2, 3]),])
def test_different_summands(n, summands):
    assert different_summands(n) == summands
