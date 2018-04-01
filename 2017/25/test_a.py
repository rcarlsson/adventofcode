import unittest
from aoc_25a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve('test_input', 'A', 6), 3)


if __name__ == '__main__':
    unittest.main()
