import unittest
from aoc_22a import *


class MyTest(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve('test_input', 7), 5)

    def test_example2(self):
        self.assertEqual(solve('test_input', 70), 41)

    def test_example3(self):
        self.assertEqual(solve('test_input', 10000), 5587)


if __name__ == '__main__':
    unittest.main()
