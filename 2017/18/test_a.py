import unittest
from aoc_18a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve('test_input_a'), 4)


if __name__ == '__main__':
    unittest.main()
