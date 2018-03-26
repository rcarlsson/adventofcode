import unittest
from aoc_15a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(65, 8921, 40000000), 588)


if __name__ == '__main__':
    unittest.main()