from unittest import TestCase

from puzzles.random.two_to_one import TwoToOne


class TestTwoToOne(TestCase):

    def test_returns_distinct_sorted_characters_from_given_strings(self):
        two_to_one = TwoToOne()

        self.assertEqual("abctw", two_to_one.longest("abc", "twac"))
