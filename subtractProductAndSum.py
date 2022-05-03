"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:
Input: n = 234
Output: 15

Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15


Runtime: 43 ms, faster than 47.10% of Python3 online submissions for Subtract the Product and Sum of Digits of an
Integer.
Memory Usage: 13.9 MB, less than 55.71% of Python3 online submissions for Subtract the Product and Sum of Digits of an
Integer.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sums = 0
        for i in str(n):
            sums += int(i)
            prod *= int(i)
        return prod - sums
