import unittest
from aoc_09a import *


class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve("{}"), 1)
        self.assertEqual(solve("{{{}}}"), 6)
        self.assertEqual(solve("{{},{}}"), 5)
        self.assertEqual(solve("{{{},{},{{}}}}"), 16)
        self.assertEqual(solve("{<a>,<a>,<a>,<a>}"), 1)
        self.assertEqual(solve("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)
        self.assertEqual(solve("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)
        self.assertEqual(solve("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)


if __name__ == '__main__':
    unittest.main()