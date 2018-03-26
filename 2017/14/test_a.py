import unittest
from aoc_14a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve("flqrgnkx"), 8108)


if __name__ == '__main__':
    unittest.main()