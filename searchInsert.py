"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
            n = len(nums)
            for i in range(n):
                if nums[i] == target:
                    return i
                else:
                    if target > nums[n-1]:
                        return n
                    elif target < nums[0]:
                        return 0
                    elif nums[i] < target < nums[i + 1]:
                        return i+1


