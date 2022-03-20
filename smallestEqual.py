"""
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1
if such index does not exist.
x mod y denotes the remainder when x is divided by y.

Runtime: 193 ms, faster than 5.19% of Python3 online submissions for Smallest Index With Equal Value.
Memory Usage: 13.8 MB, less than 96.54% of Python3 online submissions for Smallest Index With Equal Value.
"""


class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        val = -1
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                val = i
                break
        return val
