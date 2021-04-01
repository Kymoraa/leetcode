"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_total = nums[0]
        curr_total = nums[0]

        for i in range(1, len(nums)):
            curr_total = max((curr_total + nums[i]), nums[i])
            max_total = max(curr_total, max_total)

        return max_total
