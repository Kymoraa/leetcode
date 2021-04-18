"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 2 == 0:
            n = n/2

        while n % 3 == 0:
            n = n/3

        while n % 5 == 0:
            n = n/5

        return n == 1
