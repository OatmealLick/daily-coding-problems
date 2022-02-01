import pytest
from problems.daily_coding_problem_49 import max_sum_of_subarray

@pytest.mark.parametrize("nums,expected", [
    ([34, -50, 42, 14, -5, 86], 137),
    ([-5, -1, -8, -9], 0),
])
def test(nums, expected):
    assert max_sum_of_subarray(nums) == expected