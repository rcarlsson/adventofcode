import unittest
from template import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(test_data), test_result)


if __name__ == '__main__':
    unittest.main()
