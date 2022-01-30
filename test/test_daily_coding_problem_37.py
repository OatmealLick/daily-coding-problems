import pytest
from problems.daily_coding_problem_37 import top_down

@pytest.mark.parametrize("nums,expected", [
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]),
])
def test(nums, expected):
    assert sorted(top_down(nums)) == sorted(expected)
