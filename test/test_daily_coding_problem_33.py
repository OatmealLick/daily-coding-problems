import pytest
from problems.daily_coding_problem_33 import running_median

@pytest.mark.parametrize("nums,expected", [
    ([2, 1, 5, 7, 2, 0, 5], [2, 1.5, 2, 3.5, 2, 2, 2]),
])
def test(nums, expected):
    assert running_median(nums) == expected
