import unittest

from puzzles.puzzle.ArrayHighAndLowFinder import ArrayHighAndLowFinder


class ArrayHighAndLowFinderTest(unittest.TestCase):
    def test_return_correct_high_low_number_when_string_contains_all_positives(self):
        high_and_low = ArrayHighAndLowFinder()

        self.assertEqual("5 1", high_and_low.find("1 2 3 4 5"))

    def test_return_correct_high_low_number_when_string_contains_all_negatives(self):
        high_and_low = ArrayHighAndLowFinder()

        self.assertEqual("-1 -5", high_and_low.find("-1 -2 -3 -4 -5"))

    def test_return_correct_high_low_number_when_string_contains_pos_neg_numbers(self):
        high_and_low = ArrayHighAndLowFinder()

        self.assertEqual("102 -10", high_and_low.find("-1 2 -3 99 102 -10"))

    def test_return_only_number_when_string_contains_one_number(self):
        high_and_low = ArrayHighAndLowFinder()

        self.assertEqual("99 99", high_and_low.find("99"))
