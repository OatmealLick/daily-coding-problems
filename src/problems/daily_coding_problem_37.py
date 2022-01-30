def do_top_down(nums: list[int], results: list[list[int]]):
    if not nums:
        return results

    for num in nums:
        new_nums = nums.copy()
        new_nums.remove(num)
        if nums not in results:
            results.append(nums)
        do_top_down(new_nums, results)
    return results


def top_down(nums: list[int]):
    """
    The power set of a set is the set of all its subsets.
    Write a function that, given a set, generates its power set.
    For example, given the set {1, 2, 3}, it should return
      {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
    You may also use a list or array to represent a set.
    """
    results = [[]]
    do_top_down(nums, results)
    return results


def bottom_up(nums: list[int]):
    """
    0 - {}                                  = {}
    1 - f(0) + for x in f(0): x + {a}       = {}, {1}
    2 - f(1) + for x in f(1): x + {b}       = {}, {1}, {2}, {1, 2}
    3 - f(2) + for x in f(2): x + {c}       = {}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}
    """
    results = [[]]
    for i, num in enumerate(nums):
        new_results = []
        for prev_results in results:
            new_results.append(prev_results + [num])
        results = results + new_results
    return results