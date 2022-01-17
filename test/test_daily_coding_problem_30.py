import unittest
from problems.daily_coding_problem_30 import trap_water


class MyTestCase30(unittest.TestCase):

    def test_it(self):
        input = [3, 0, 1, 3, 0, 5]
        output = 8
        self.assertEqual(trap_water(input), output)

    def test_silly_example(self):
        input = [2, 1, 2]
        output = 1
        self.assertEqual(trap_water(input), output)

if __name__ == '__main__':
    unittest.main()
