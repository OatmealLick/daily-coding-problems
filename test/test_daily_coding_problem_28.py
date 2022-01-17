import unittest
from problems.daily_coding_problem_28 import justify


class MyTestCase28(unittest.TestCase):

    def test_it(self):
        words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        justified = ["the  quick brown",
                     "fox  jumps  over",
                     "the   lazy   dog"]
        self.assertEqual(justify(words, 16), justified)


if __name__ == '__main__':
    unittest.main()
