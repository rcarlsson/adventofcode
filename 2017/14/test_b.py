import unittest
from aoc_14b import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve("flqrgnkx"), 1242)

    def test_clear_group(self):
        data = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(clear_group(data, 2, 2), result)

    def test_calc_groups(self):
        data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(calc_groups(data), 0)

        data = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        self.assertEqual(calc_groups(data), 1)

        data = [[0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0]]
        self.assertEqual(calc_groups(data), 3)


if __name__ == '__main__':
    unittest.main()