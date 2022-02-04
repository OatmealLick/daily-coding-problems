from datetime import datetime
from typing import Any


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        self.timestamp = datetime.utcnow()

    def __str__(self):
        return f"[{self.key}: {self.value}] -> {self.next}"

    def __repr__(self):
        return str(self)


class LeastRecentlyUsedCache:
    """
    Implement an LRU (Least Recently Used) cache.
    It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value.
      If there are already n items in the cache and we are adding a new item,
      then it should also remove the least recently used item.
    get(key): gets the value at key.
      If no such key exists, return null.

    Each operation should run in O(1) time.
    """

    def __init__(self, size: int):
        self.size = size
        self.references: dict[Any, Node] = {}
        self.head: Node = None
        self.tail: Node = None

    def __str__(self):
        return f"ref {self.references}, head {self.head}"

    def get(self, key: Any):
        if key not in self.references:
            return None
        node = self.references[key]
        self._remove_node(node)
        self._add_node(key, node.value)

    def set(self, key, value):
        if key in self.references:
            node = self.references[key]
            self._remove_node(node)
            self._add_node(key, value)
        elif len(self.references) < self.size:
            self._add_node(key, value)
        else:
            self.references.pop(self.tail.key)
            self.tail = self.tail.next
            self._add_node(key, value)

    def _remove_node(self, node):
        if node.next is not None and self.tail == node:
            self.tail = node.next
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def _add_node(self, key, value):
        new_node = Node(key, value, prev=self.head)
        if self.head is not None:
            self.head.next = new_node
        if self.tail is None:
            self.tail = new_node

        self.head = new_node
        self.references[key] = new_node
