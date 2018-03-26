import unittest
from aoc_07a import *

class MyTest(unittest.TestCase):
	def test_example(self):
		with open('test_input') as f:
			self.assertEqual(solve(f),'tknk')

if __name__ == '__main__':
    unittest.main()