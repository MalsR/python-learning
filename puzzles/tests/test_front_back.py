from unittest import TestCase

from puzzles.codingbat.warmup_1.front_back import FrontBack


class TestFrontBack(TestCase):

    def test_returns_string_with_front_rear_chars_swapped(self):
        front_back = FrontBack()

        self.assertEqual("oellH", front_back.front_back("Hello"))

    def test_returns_string_when_length_is_one(self):
        front_back = FrontBack()

        self.assertEqual("X", front_back.front_back("X"))

    def test_returns_string_front_rear_chars_swapped_when_length_two(self):
        front_back = FrontBack()

        self.assertEqual("ba", front_back.front_back("ab"))

    def test_returns_string_front_rear_chars_swapped_when_length_three(self):
        front_back = FrontBack()

        self.assertEqual("cba", front_back.front_back("abc"))

