"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


First thought of doing a bubble sort type of algorithm, where I bubble the zeros to the right.
The algo worked for some test cases but failed for others because it switched the order for other non zero values.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pos = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr != 0:
                temp = nums[pos]
                nums[pos] = nums[i]
                nums[i] = temp
                pos += 1
