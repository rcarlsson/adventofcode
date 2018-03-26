import unittest
from aoc_16a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        programs = 'abcde'
        self.assertEqual(execute_commands(['s1', 'x3/4', 'pe/b'], programs), 'baedc')


if __name__ == '__main__':
    unittest.main()