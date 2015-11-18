from collections import namedtuple
from unittest import TestCase

from src.module_3.continuous_backpack import continuous_backpack


class TestSectionDotCoverage(TestCase):

    def test_returns_correct_result(self):
        Thing = namedtuple('Thing', ['price', 'weight'])
        self.assertEqual(
            continuous_backpack(
                50, [Thing(60, 20), Thing(100, 50), Thing(120, 30)]
            ),
            180
        )
