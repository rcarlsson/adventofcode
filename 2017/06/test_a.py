import unittest
from aoc_06a import *

class MyTest(unittest.TestCase):
	def test_example(self):
		self.assertEqual(solve([0,2,7,0]),5)

if __name__ == '__main__':
    unittest.main()