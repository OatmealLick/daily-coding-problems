from typing import Any


class TwoStackQueue:
    """
    Implement a queue using two stacks.

    Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:
    enqueue, which inserts an element into the queue, and dequeue, which removes it.
    """

    def __init__(self):
        self.enqueue_stack: list[Any] = []
        self.dequeue_stack: list[Any] = []

    def enqueue(self, value: Any):
        while self.dequeue_stack:
            self.enqueue_stack.append(self.dequeue_stack.pop())
        self.enqueue_stack.append(value)

    def dequeue(self) -> Any:
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
