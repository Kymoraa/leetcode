"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and
maximize the product of those integers.

Return the maximum product you can get.

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Solved using the idea that when you break down a number into it twos and threes, the product of these will be the
maximum

"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return n-1
        threes = n // 3
        remainder = n % 3
        if remainder == 1:
            threes -= 1
            twos = 2
        elif remainder == 2:
            twos = 1
        else:
            twos = 0

        result = (3**threes) * (2**twos)
        return result
