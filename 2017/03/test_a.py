import unittest
from aoc_03a import *

class MyTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(calcPathLength(1), 0)

	def test2(self):
		self.assertEqual(calcPathLength(2), 1)

	def test3(self):
		self.assertEqual(calcPathLength(3), 2)

	def test4(self):
		self.assertEqual(calcPathLength(4), 1)

	def test5(self):
		self.assertEqual(calcPathLength(5), 2)

	def test6(self):
		self.assertEqual(calcPathLength(6), 1)

	def test7(self):
		self.assertEqual(calcPathLength(7), 2)

	def test8(self):
		self.assertEqual(calcPathLength(8), 1)

	def test9(self):
		self.assertEqual(calcPathLength(9), 2)

	def test10(self):
		self.assertEqual(calcPathLength(10), 3)

	def test11(self):
		self.assertEqual(calcPathLength(11), 2)

	def test12(self):
		self.assertEqual(calcPathLength(12), 3)

	def test13(self):
		self.assertEqual(calcPathLength(13), 4)

	def test14(self):
		self.assertEqual(calcPathLength(14), 3)

	def test15(self):
		self.assertEqual(calcPathLength(15), 2)

	def test16(self):
		self.assertEqual(calcPathLength(16), 3)

	def test17(self):
		self.assertEqual(calcPathLength(17), 4)

	def test18(self):
		self.assertEqual(calcPathLength(18), 3)

	def test19(self):
		self.assertEqual(calcPathLength(19), 2)

	def test20(self):
		self.assertEqual(calcPathLength(20), 3)

	def test21(self):
		self.assertEqual(calcPathLength(21), 4)

	def test22(self):
		self.assertEqual(calcPathLength(22), 3)

	def test23(self):
		self.assertEqual(calcPathLength(23), 2)

	def test24(self):
		self.assertEqual(calcPathLength(24), 3)

	def test25(self):
		self.assertEqual(calcPathLength(25), 4)

	def test26(self):
		self.assertEqual(calcPathLength(26), 5)

	def test27(self):
		self.assertEqual(calcPathLength(27), 4)

	def test31(self):
		self.assertEqual(calcPathLength(31), 6)

	def test32(self):
		self.assertEqual(calcPathLength(32), 5)

	def test33(self):
		self.assertEqual(calcPathLength(33), 4)

	def test34(self):
		self.assertEqual(calcPathLength(34), 3)

	def test1024(self):
		self.assertEqual(calcPathLength(1024), 31)

if __name__ == '__main__':
    unittest.main()