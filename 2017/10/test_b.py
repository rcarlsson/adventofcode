import unittest
from aoc_10b import *


class MyTest(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve_line(256, ""), "a2582a3a0e66e6e86e3812dcb672a272")

    def test_example2(self):
        self.assertEqual(solve_line(256, "AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")

    def test_example3(self):
        self.assertEqual(solve_line(256, "1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")

    def test_example4(self):
        self.assertEqual(solve_line(256, "1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")


if __name__ == '__main__':
    unittest.main()