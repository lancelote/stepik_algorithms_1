import pytest

from src.module_4.section_dot_coverage import section_dot_coverage, Section


@pytest.mark.parametrize(
    "sections,dots",
    [
        ([Section(1, 3), Section(2, 5), Section(3, 6)], [3]),
        ([Section(4, 6), Section(1, 3), Section(2, 5), Section(5, 6)], [3, 6]),
    ],
)
def test_section_dot_coverage(sections, dots):
    assert section_dot_coverage(sections) == dots
