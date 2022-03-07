"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Runtime: 81 ms, faster than 25.02% of Python3 online submissions for Add Strings.
Memory Usage: 14.1 MB, less than 67.84% of Python3 online submissions for Add Strings.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1) - 1
        m = len(num2) - 1
        carry = 0
        output = ""

        while n >= 0 and m >= 0:
            sums = int(num1[n]) + int(num2[m]) + carry
            val = sums % 10
            if sums >= 10:
                carry = 1
            else:
                carry = 0
            output = str(val) + output
            n -= 1
            m -= 1

        while n >= 0:
            sums = int(num1[n]) + carry
            val = sums % 10
            if sums >= 10:
                carry = 1
            else:
                carry = 0
            output = str(val) + output
            n -= 1

        while m >= 0:
            sums = int(num2[m]) + carry
            val = sums % 10
            if sums >= 10:
                carry = 1
            else:
                carry = 0
            output = str(val) + output
            m -= 1
        if carry:
            output = str(carry) + output

        return output
