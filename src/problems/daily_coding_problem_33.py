from heapq import heappop, heappush

def running_median(nums: list[int]):
    """
    Compute the running median of a sequence of numbers.
    That is, given a stream of numbers, print out the median of the list so far on each new element.
    Recall that the median of an even-numbered list is the average of the two middle numbers.

    For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
    [2, 1.5, 2, 3.5, 2, 2, 2]
    """
    max_heap = []
    min_heap = []

    medians = []
    for i, num in enumerate(nums):
        if i == 0:
            heappush(min_heap, num)
            medians.append(num)
            continue

        if min_heap[0] < num:
            heappush(min_heap, num)
        else:
            heappush(max_heap, -num)

        if len(min_heap) - len(max_heap) > 1:
            min_root = heappop(min_heap)
            heappush(max_heap, -min_root)
        elif len(max_heap) - len(min_heap) > 1:
            max_root = heappop(max_heap)
            heappush(min_heap, -max_root)

        if i % 2 == 1:
            medians.append((min_heap[0] - max_heap[0]) / 2)
        elif len(max_heap) > len(min_heap):
            medians.append(-max_heap[0])
        else:
            medians.append(min_heap[0])

    return medians
