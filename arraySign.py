"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Stats:
Runtime: 74 ms, faster than 61.46% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 14 MB, less than 38.37% of Python3 online submissions for Sign of the Product of an Array.

//N.B Came across this solution and I think it's pretty nifty
def arraySign(self, nums: List[int]) -> int:
		negative = 1
		for number in nums:
			if number == 0:
				return 0
			elif number < 0:
				negative *= -1
		return negative
"""


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        prod = nums[0]
        for i in range(1, len(nums)):
            prod *= nums[i]
        if prod < 0:
            return -1
        elif prod > 0:
            return 1
        else:
            return 0
