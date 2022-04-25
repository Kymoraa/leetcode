"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its
binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
So you need to output 2.

Runtime: 58 ms, faster than 12.14% of Python3 online submissions for Number Complement.
Memory Usage: 13.8 MB, less than 54.20% of Python3 online submissions for Number Complement.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        res = ""
        n = bin(num)[2:]
        for i in n:
            if i == '1':
                res += '0'
            else:
                res += '1'

        return int(res, 2)
