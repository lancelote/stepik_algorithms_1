import pytest

from src.module_4.huffman_decode import decode


@pytest.mark.parametrize(
    "encoded_string,decode_dict,decoded_string",
    [
        ("0", {"0": "a"}, "a"),
        (
            "01001100100111",
            {"0": "a", "10": "b", "110": "c", "111": "d"},
            "abacabad",
        ),
        ("1111100000", {"0": "y", "1": "z"}, "zzzzzyyyyy"),
    ],
)
def test_decode(encoded_string, decode_dict, decoded_string):
    assert decode(encoded_string, decode_dict) == decoded_string
