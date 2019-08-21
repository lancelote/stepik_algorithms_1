from unittest import TestCase

from module_3.section_dot_coverage import section_dot_coverage


class TestSectionDotCoverage(TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(
            section_dot_coverage([(1, 3), (2, 5), (3, 6)]),
            [1, [3]]
        )
        self.assertEqual(
            section_dot_coverage([(4, 7), (1, 3), (2, 5), (5, 6)]),
            [2, [3, 6]]
        )
