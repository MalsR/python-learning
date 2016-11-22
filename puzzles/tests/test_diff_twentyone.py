from unittest import TestCase

from puzzles.codingbat.diff_twentyone import DiffTwentyOne


class TestDiffTwentyOne(TestCase):

    def test_returns_absolute_diff_when_number_is_greater_than_zero_less_than_twentyone(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(16, diff_twenty_one.diff_twentyone(5))

    def test_returns_absolute_diff_when_number_is_greater_than_twentyone(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(8, diff_twenty_one.diff_twentyone(25))

    def test_returns_zero_when_number_is_twentyone(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(0, diff_twenty_one.diff_twentyone(21))

    def test_returns_absolute_diff_when_number_is_less_than_zero(self):
        diff_twenty_one = DiffTwentyOne()

        self.assertEqual(24, diff_twenty_one.diff_twentyone(-3))
