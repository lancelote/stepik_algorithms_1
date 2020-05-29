import pytest

from module_4.section_dot_coverage import section_dot_coverage


@pytest.mark.parametrize(
    "sections,dots",
    [
        ([(1, 3), (2, 5), (3, 6)], [3]),
        ([(4, 6), (1, 3), (2, 5), (5, 6)], [3, 6]),
    ],
)
def test_section_dot_coverage(sections, dots):
    assert section_dot_coverage(sections) == dots
