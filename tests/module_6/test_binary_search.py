from typing import List

import pytest

from src.module_6.binary_search import bin_find


@pytest.fixture
def odd_array() -> List[int]:
    return [1, 5, 8, 12, 13]


@pytest.fixture
def even_array() -> List[int]:
    return [1, 5, 8, 12]


@pytest.mark.parametrize(
    "item,index", [(8, 2), (1, 0), (23, -1), (1, 0), (11, -1), (0, -1)]
)
def test_bin_find_odd_array(item, odd_array, index):
    assert bin_find(item, odd_array) == index


@pytest.mark.parametrize(
    "item,index", [(8, 2), (1, 0), (23, -1), (1, 0), (11, -1), (0, -1)]
)
def test_bin_find_even_array(item, even_array, index):
    assert bin_find(item, even_array) == index
