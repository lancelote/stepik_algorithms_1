from unittest import TestCase

from module_3.different_summands import different_summands


class TestSectionDotCoverage(TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(different_summands(4), [2, [1, 3]])
        self.assertEqual(different_summands(6), [3, [1, 2, 3]])
