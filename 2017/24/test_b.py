import unittest
from aoc_24b import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve('test_input'), 19)


if __name__ == '__main__':
    unittest.main()
