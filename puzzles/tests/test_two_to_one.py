from unittest import TestCase

from puzzles.random.two_to_one import TwoToOne


class TestTwoToOne(TestCase):

    def test_returns_distinct_characters_from_given_strings_in_alphabetical_order(self):
        two_to_one = TwoToOne()

        self.assertEqual("abctw", two_to_one.longest("abc", "twac"))

    def test_returns_empty_string_when_given_strings_are_empty(self):
        two_to_one = TwoToOne()

        self.assertEqual("", two_to_one.longest("", ""))

    def test_returns_distinct_characters_from_given_strings_in_alphabetical_order_when_first_string_empty(self):
        two_to_one = TwoToOne()

        self.assertEqual("actw", two_to_one.longest("", "twac"))

    def test_returns_distinct_characters_from_given_strings_in_alphabetical_order_when_second_string_empty(self):
        two_to_one = TwoToOne()

        self.assertEqual("bcz", two_to_one.longest("cbz", ""))
