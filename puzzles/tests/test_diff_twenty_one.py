from unittest import TestCase

from puzzles.codingbat.diff_twentyone import DiffTwentyOne


class TestDiffTwentyOne(TestCase):

    def test_returns_absolute_diff_when_number_is_greater_than_zero_less_than_twenty_one(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(16, diff_twenty_one.diff_twenty_one(5))

    def test_returns_absolute_diff_when_number_is_greater_than_twenty_one(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(8, diff_twenty_one.diff_twenty_one(25))

    def test_returns_zero_when_number_is_twenty_one(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(0, diff_twenty_one.diff_twenty_one(21))

    def test_returns_absolute_diff_when_number_is_less_than_zero(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(24, diff_twenty_one.diff_twenty_one(-3))
