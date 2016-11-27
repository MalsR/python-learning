from unittest import TestCase

from puzzles.codingbat.warmup_1.missing_char import MissingChar


class TestMissingChar(TestCase):

    def test_returns_string_without_given_char_index(self):
        missing_char = MissingChar()

        self.assertEqual("Tst", missing_char.missing_char("Test", 1))
        self.assertEqual("est", missing_char.missing_char("Test", 0))
        self.assertEqual("Tet", missing_char.missing_char("Test", 2))
        self.assertEqual("Tes", missing_char.missing_char("Test", 3))

    def test_returns_string_without_given_char_index_another_way(self):
        missing_char = MissingChar()

        self.assertEqual("Tst", missing_char.missing_char_shorter_way("Test", 1))
        self.assertEqual("est", missing_char.missing_char_shorter_way("Test", 0))
        self.assertEqual("Tet", missing_char.missing_char_shorter_way("Test", 2))
        self.assertEqual("Tes", missing_char.missing_char_shorter_way("Test", 3))
