import sys

def max_sum_of_subarray(nums: list[int]) -> int:
    """
    Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
    For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
    since we would take elements 42, 14, -5, and 86.
    Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
    Do this in O(N) time.
    """
    max_sum = 0
    current_sum = 0
    for num in nums:
        if current_sum + num > 0:
            current_sum += num
        else:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
    return max_sum