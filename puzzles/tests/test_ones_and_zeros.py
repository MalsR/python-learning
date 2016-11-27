from unittest import TestCase

from puzzles.random.ones_and_zeros import OnesAndZeros


class TestOnesAndZeros(TestCase):

    def test_returns_zero_from_binary_represented_array(self):
        ones_and_zeros = OnesAndZeros()

        self.assertEqual(0, ones_and_zeros.ones_and_zeros([0, 0, 0, 0]))

    def test_returns_one_from_binary_represented_array(self):
        ones_and_zeros = OnesAndZeros()

        self.assertEqual(1, ones_and_zeros.ones_and_zeros([0, 0, 0, 1]))

    def test_returns_two_from_binary_represented_array(self):
        ones_and_zeros = OnesAndZeros()

        self.assertEqual(2, ones_and_zeros.ones_and_zeros([0, 0, 1, 0]))

    def test_returns_three_from_binary_represented_array(self):
        ones_and_zeros = OnesAndZeros()

        self.assertEqual(3, ones_and_zeros.ones_and_zeros([0, 0, 1, 1]))

    def test_returns_nine_from_binary_represented_array(self):
        ones_and_zeros = OnesAndZeros()

        self.assertEqual(9, ones_and_zeros.ones_and_zeros([1, 0, 0, 1]))

    def test_returns_eight_hundred_from_binary_represented_array(self):
        ones_and_zeros = OnesAndZeros()

        self.assertEqual(800, ones_and_zeros.ones_and_zeros([1, 1, 0, 0, 1, 0, 0, 0, 0, 0]))
