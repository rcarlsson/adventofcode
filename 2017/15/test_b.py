import unittest
from aoc_15b import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(65, 8921, 5000000), 309)


if __name__ == '__main__':
    unittest.main()