from utils.binary_tree import Node


def compute_tree(node: Node) -> int:
    """
    Suppose an arithmetic expression is given as a binary tree.
    Each leaf is an integer and each internal node is one of '+', '−', '∗', or '\/'.
    Given the root to such a tree, write a function to evaluate it.
    For example, given the following tree:

             *
            / \
          +    +
         / \  / \
        3  2  4  5

    You should return 45, as it is (3 + 2) * (4 + 5).
    """
    if node.left is None and node.right is None:
        return int(node.value)
    left = compute_tree(node.left)
    right = compute_tree(node.right)
    return _perform_arithmetic(node.value, left, right)


def _perform_arithmetic(op, a, b):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "-":
        return a - b
    else:
        return a // b
