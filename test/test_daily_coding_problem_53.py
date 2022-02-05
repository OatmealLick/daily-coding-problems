from problems.daily_coding_problem_53 import TwoStackQueue


def test_have_fifo_order():
    queue = TwoStackQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(4)
    queue.enqueue(6)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 4
