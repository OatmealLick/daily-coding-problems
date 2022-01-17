import unittest
from problems.daily_coding_problem_29 import encode


class MyTestCase29(unittest.TestCase):

    def test_it(self):
        input = "AAAABBBCCDAA"
        output = "4A3B2C1D2A"
        self.assertEqual(encode(input), output)


if __name__ == '__main__':
    unittest.main()
