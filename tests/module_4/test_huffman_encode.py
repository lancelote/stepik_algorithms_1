import pytest

from src.module_4.huffman_code import Tree


@pytest.mark.parametrize(
    "string,expected", [("a", "0"), ("abacabad", "01001100100111")]
)
def test_encoding(string, expected):
    assert Tree.from_string(string).encoded_string == expected
