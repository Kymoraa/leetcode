"""
Given an array nums of integers, return how many of them contain an even number of digits.

Example:
Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.

Stats:
Runtime: 60 ms, faster than 74.98% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 13.8 MB, less than 98.99% of Python3 online submissions for Find Numbers with Even Number of Digits.
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
