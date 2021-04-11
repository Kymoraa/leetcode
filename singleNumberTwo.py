"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

Example 1:

Input: nums = [2,2,3,2]
Output: 3

"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        memo = {}

        for i in nums:
            if i in memo:
                memo[i] += 1
            else:
                memo[i] = 1
        return list(memo.keys())[list(memo.values()).index(1)]

