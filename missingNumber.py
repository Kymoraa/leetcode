"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that
is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

First, I went the sort route...
Where by, once you have sorted the array the missing number will be where value at i != i+1

Other option is using a set. Place all the nums in the set and loop from 0 to n+1
Return the number not in the set

Other option is using the Gauss formula as below
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        for i in range(n):
            total -= nums[i]
        return total
