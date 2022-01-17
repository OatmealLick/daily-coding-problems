import pytest

from problems.daily_coding_problem_31 import naive_levenshtein_distance, dp_levenshtein_distance, dp_iterative_levenshtein_distance


@pytest.mark.parametrize("a,b,expected", [
    ("kitten", "sitting", 3),
    ("dupa", "adup", 2),
    ("abcdefghijk", "cbdajklghif", 8),
    ("aaaaaa", "aaaaaa", 0)
])
def test_naive(a, b, expected):
    assert naive_levenshtein_distance(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    ("kitten", "sitting", 3),
    ("dupa", "adup", 2),
    ("abcdefghijk", "cbdajklghif", 8),
    ("aaaaaaaaaaaa", "aaaaaaaaaaaa", 0)
])
def test_dp(a, b, expected):
    assert dp_levenshtein_distance(a, b, {}) == expected


@pytest.mark.parametrize("a,b,expected", [
    ("kitten", "sitting", 3),
    ("dupa", "adup", 2),
    ("abcdefghijk", "cbdajklghif", 8),
    ("aaaaaaaaaaaa", "aaaaaaaaaaaa", 0)
])
def test_dp(a, b, expected):
    assert dp_iterative_levenshtein_distance(a, b) == expected
