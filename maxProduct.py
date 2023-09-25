"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Brute force : time complexity = O (n^2)

def maxProduct(nums):
    max_prod = -math.inf
    for i in range(len(nums)):
        curr_prod = 1
        for j in range(i, len(nums)):
            curr_prod *= nums[j]
            max_prod = max(curr_prod, max_prod)
    return max_prod

"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod, curr_max, curr_min = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            temp = curr_max * num
            curr_max = max(temp, curr_min * num, num)
            curr_min = min(temp, curr_min * num, num)
            max_prod = max(max_prod, curr_max)
        return max_prod
