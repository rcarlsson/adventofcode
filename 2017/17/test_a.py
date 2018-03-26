import unittest
from aoc_17a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(3, 2017), 638)


if __name__ == '__main__':
    unittest.main()
