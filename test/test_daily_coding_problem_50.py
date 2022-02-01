import pytest
from problems.daily_coding_problem_50 import compute_tree
from utils.binary_tree import Node


@pytest.mark.parametrize("tree,expected", [
    (Node("*", Node("+", Node("3"), Node("2")), Node("+", Node("4"), Node("5"))), 45)
])
def test(tree, expected):
    assert compute_tree(tree) == expected