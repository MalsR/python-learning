from unittest import TestCase

from puzzles.random.parity_outlier import ParityOutlier


class TestParityOutlier(TestCase):

    def test_returns_odd_number_when_all_other_numbers_are_even(self):
        parity_outlier = ParityOutlier()
        numbers_to_find = [2, 4, 3, 8, 100, 200]

        self.assertEqual(3, parity_outlier.find(numbers_to_find))

    def test_returns_even_number_when_other_numbers_are_odd(self):
        parity_outlier = ParityOutlier()
        numbers_to_find = [0, 1, 2, 4, 6, 88, 102]

        self.assertEqual(1, parity_outlier.find(numbers_to_find))

    def test_returns_negative_odd_number_when_other_numbers_are_even(self):
        parity_outlier = ParityOutlier()
        numbers_to_find = [2, 4, -3, 8, 100, 220]

        self.assertEqual(-3, parity_outlier.find(numbers_to_find))

    def test_returns_negative_even_number_when_other_numbers_are_odd(self):
        parity_outlier = ParityOutlier()
        numbers_to_find = [3, 5, 7, 99, -102]

        self.assertEqual(-102, parity_outlier.find(numbers_to_find))

#    TODO Add exception example
