"""
Given integer array nums, return the third maximum number in this array.
If the third maximum does not exist, return the maximum number.

Used sorting and sets
"""


class Solution:
    def thirdMax(self, nums) -> int:
        values = list(set(nums))
        if len(values) < 3:
            return max(values)
        else:
            values.sort(reverse=True)
            return values[2]
