"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Solution:
Convert list to int by first converting to string
Add the ints
Convert back to list via string

Stats:
Runtime: 512 ms, faster than 33.33% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 14.6 MB, less than 92.66% of Python3 online submissions for Add to Array-Form of Integer.
"""


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        str_num = ""
        for i in num:
            str_num = str_num + str(i)
        sum_nums = int(str_num) + k
        return list(str(sum_nums))
