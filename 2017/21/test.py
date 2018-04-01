import unittest
from aoc_21 import *


class MyTest(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(rotate_grid(['12', '34']), ['31', '42'])
        self.assertEqual(rotate_grid(['123', '456', '789']), ['741', '852', '963'])

    def test_flip(self):
        self.assertEqual(flip_grid(['12', '34']), ['21', '43'])
        self.assertEqual(flip_grid(['123', '456', '789']), ['321', '654', '987'])

    def test_get_variations(self):
        test_input = ['12', '34']
        test_output = [['12', '34'], ['31', '42'], ['43', '21'], ['24', '13'], ['21', '43'], ['42', '31'], ['34', '12'], ['13', '24']]
        self.assertEqual(get_all_variations(test_input), test_output)


if __name__ == '__main__':
    unittest.main()
