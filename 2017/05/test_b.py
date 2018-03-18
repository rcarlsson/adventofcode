import unittest
from aoc_05b import *

class MyTest(unittest.TestCase):
	def test_example(self):
		self.assertEqual(solve([0,3,0,1,-3]),10)

if __name__ == '__main__':
    unittest.main()