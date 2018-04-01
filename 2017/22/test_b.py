import unittest
from aoc_22b import *


class MyTest(unittest.TestCase):
    def test_example0(self):
        self.assertEqual(solve('test_input', 7), 1)

    def test_example1(self):
        self.assertEqual(solve('test_input', 100), 26)

    def test_example2(self):
        self.assertEqual(solve('test_input', 10000000), 2511944)


if __name__ == '__main__':
    unittest.main()
