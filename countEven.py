"""
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are
even.

The digit sum of a positive integer is the sum of all its digits.

Example 1:
Input: num = 4
Output: 2

Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.

Stats
Runtime: 103 ms, faster than 6.07% of Python3 online submissions for Count Integers With Even Digit Sum.
Memory Usage: 14 MB, less than 12.62% of Python3 online submissions for Count Integers With Even Digit Sum.
"""


class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        sums = 0
        for i in range(1, num+1):
            sums = sum(int(j) for j in str(i))
            if sums%2 == 0:
                count += 1
        return count
