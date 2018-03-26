import unittest
from aoc_09b import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve("<>"), 0)
        self.assertEqual(solve("<random characters>"), 17)
        self.assertEqual(solve("<<<<>"), 3)
        self.assertEqual(solve("<{!>}>"), 2)
        self.assertEqual(solve("<!!>"), 0)
        self.assertEqual(solve("<!!!>>"), 0)
        self.assertEqual(solve("<{o\"i!a,<{i<a>"), 10)


if __name__ == '__main__':
    unittest.main()