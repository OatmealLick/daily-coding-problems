class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} {self.value} {self.right})"

    def __repr__(self):
        return str(self)
