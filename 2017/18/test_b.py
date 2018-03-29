import unittest
from aoc_18b import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve('test_input_b'), 3)


if __name__ == '__main__':
    unittest.main()
