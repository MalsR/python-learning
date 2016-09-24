import unittest

from puzzles.CompareThePattern1 import CompareThePattern1


class CompareThePattern1Test(unittest.TestCase):
    def test_upper(self):
        compare_the_pattern = CompareThePattern1()

        expected_pattern = "1\n22"

        self.assertEqual(expected_pattern, compare_the_pattern.pattern(2))


if __name__ == '__main__':
    unittest.main()
