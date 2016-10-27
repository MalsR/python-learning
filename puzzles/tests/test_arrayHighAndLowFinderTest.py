import unittest

from puzzles.puzzle.ArrayHighAndLowFinder import ArrayHighAndLowFinder


class ArrayHighAndLowFinderTest(unittest.TestCase):

    def test_return_correct_high_low_number_when_string_contains_all_positives(self):
        self.assertEqual("5 1", ArrayHighAndLowFinder().find("1 2 3 4 5"))

    def test_returns_correct_high_low_number_when_string_contains_all_negatives(self):
        self.assertEqual("-1 -5", ArrayHighAndLowFinder().find("-1 -2 -3 -4 -5"))

    def test_returns_correct_high_low_number_when_string_contains_number_mixture(self):
        self.assertEqual("542 -214", ArrayHighAndLowFinder().find("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

    def test_return_only_number_when_string_contains_one_number(self):
        self.assertEqual("99 99", ArrayHighAndLowFinder().find("99"))

    def test_returns_one_one_when_string_contains_one_one(self):
        self.assertEqual("1 1", ArrayHighAndLowFinder().find("1 1"))

    def test_returns_only_number_when_string_contains_same_number_twice(self):
        self.assertEqual("102 102", ArrayHighAndLowFinder().find("102 102"))

    def test_returns_same_number_pos_and_neg_when_string_contains_same(self):
        self.assertEqual("8 -8", ArrayHighAndLowFinder().find("-8 8"))

    def test_returns_high_and_low_when_string_contains_number_mixture_with_zero(self):
        self.assertEqual("99 0", ArrayHighAndLowFinder().find("0 88 98 99 3"))

    def test_returns_high_and_low_when_string_contains_zero_and_negative_numbers(self):
        self.assertEqual("1 -1", ArrayHighAndLowFinder().find("0 -1 1"))
