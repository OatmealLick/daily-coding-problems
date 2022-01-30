import pytest
from problems.daily_coding_problem_37 import top_down, bottom_up


@pytest.mark.parametrize("nums,expected", [
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]),
])
def test_bottom_up(nums, expected):
    assert sorted(bottom_up(nums)) == sorted(expected)

@pytest.mark.parametrize("nums,expected", [
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]),
])
def test_top_down(nums, expected):
    assert sorted(top_down(nums)) == sorted(expected)
