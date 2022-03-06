"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Solution:
Use the built-in int() function, and pass it the base of the input number, i.e. 2 for a binary number
Sum the numbers then convert to binary, leave the first two indices out

Stats:
Runtime: 24 ms, faster than 99.33% of Python3 online submissions for Add Binary.
Memory Usage: 14 MB, less than 61.91% of Python3 online submissions for Add Binary.

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sums = (int(a, 2)) + (int(b, 2))
        return (bin(sums))[2:]
