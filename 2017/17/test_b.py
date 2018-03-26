import unittest
from aoc_17b import *


class MyTest(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(9, solve(3, 9))

    def test_example2(self):
        self.assertEqual(1226, solve(3, 2017))


if __name__ == '__main__':
    unittest.main()
