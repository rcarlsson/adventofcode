import unittest
from aoc_10a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve_line(5, "3,4,1,5"), 12)


if __name__ == '__main__':
    unittest.main()