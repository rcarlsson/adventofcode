import unittest
from aoc_03b import *

class MyTest(unittest.TestCase):
	def test_accumulate(self):
		w, h = 3, 3
		Matrix = [[0 for x in range(w)] for y in range(h)]
		Matrix[0][0] = 1
		Matrix[0][1] = 2
		Matrix[0][2] = 3
		Matrix[1][0] = 4
		Matrix[1][2] = 5
		Matrix[2][0] = 6
		Matrix[2][1] = 7
		Matrix[2][2] = 8
		self.assertEqual(accumulate(Matrix, 1, 1), 36)

if __name__ == '__main__':
    unittest.main()