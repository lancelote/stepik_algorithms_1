from collections import deque

import pytest

from src.module_4.huffman_decode import Node


@pytest.fixture
def codes():
    return {
        "a": deque("0"),
        "b": deque("10"),
        "c": deque("110"),
        "d": deque("111"),
    }


def test_from_codes(codes):
    root = Node.from_codes(codes)
    assert root.left.char == "a"
    assert root.right.left.char == "b"
    assert root.right.right.left.char == "c"
    assert root.right.right.right.char == "d"


def test_decode(codes):
    tree = Node.from_codes(codes)
    assert tree.decode("01001100100111") == "abacabad"
