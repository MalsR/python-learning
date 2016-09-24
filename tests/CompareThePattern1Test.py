import unittest

from puzzles.CompareThePattern1 import CompareThePattern1


class CompareThePattern1Test(unittest.TestCase):

    def test_return_correct_pattern_when_number_is_two(self):
        compare_the_pattern = CompareThePattern1()

        expected_pattern = "1\n22"

        self.assertEqual(expected_pattern, compare_the_pattern.pattern(2))

    def test_return_correct_pattern_when_number_is_five(self):
        compare_the_pattern = CompareThePattern1()

        expected_pattern =  "1\n22\n333\n4444\n55555"

        self.assertEqual(expected_pattern, compare_the_pattern.pattern(5))

    def test_return_correct_pattern_when_number_is_eleven(self):
        compare_the_pattern = CompareThePattern1()

        expected_pattern = "1\n" + \
                           "22\n" + \
                           "333\n" + \
                           "4444\n" + \
                           "55555\n" + \
                           "666666\n" + \
                           "7777777\n" + \
                           "88888888\n" + \
                           "999999999\n" + \
                           "10101010101010101010\n" + \
                           "1111111111111111111111"

        self.assertEqual(expected_pattern, compare_the_pattern.pattern(11))

    def test_return_empty_when_number_is_negative(self):
        pattern_generator = CompareThePattern1()

        self.assertEqual("", pattern_generator.pattern(-2))

    def test_return_empty_when_number_is_zero(self):
        pattern_generator = CompareThePattern1()

        self.assertEqual("", pattern_generator.pattern(0))

    if __name__ == '__main__':
        unittest.main()
