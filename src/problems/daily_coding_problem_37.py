def do_top_down(nums: list[int], results: list[list[int]]):
    if not nums:
        return results

    for num in nums:
        new_nums = nums.copy()
        new_nums.remove(num)
        if nums not in results:
            results.append(nums)
        do_top_down(new_nums, results)

    # todo cache?
    # todo bottom up
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

