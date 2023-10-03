"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

// this solution works, but it exceeds time limit for some test cases. (recursion calls for large inputs)
// use DP instead
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def helper(i, sum1, sum2):
            if i >= len(nums):
                return sum1 == sum2
            return helper(i + 1, sum1 + nums[i], sum2) or helper(i + 1, sum1, sum2 + nums[i])

        return helper(0, 0, 0)
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        partition_sum = sum(nums) // 2

        # boolean array with indices for the possible sums.
        dp = [False] * (partition_sum + 1)

        # first element is True i.e. possibility of a sum of 0 (an empty partition)
        dp[0] = True

        # bottom-up approach
        for num in nums:
            for j in range(partition_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]  # not including or including the current number
        return dp[partition_sum]
