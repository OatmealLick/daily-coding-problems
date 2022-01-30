import pytest
from problems.daily_coding_problem_47 import profit

@pytest.mark.parametrize("nums,expected", [
    ([9, 11, 8, 5, 7, 10], 5),
    ([2, 1, 6, 3, 8, 3, 7], 7),
])
def test(nums, expected):
    assert profit(nums) == expected
