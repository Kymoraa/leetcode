"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Solution: Converted the number to a string and reversed it
A palindrome number when reversed should be equal to the original

Ps. I found a simplified one liner for the code I have...
Just basically maintain the reversed and the original as strings. No need to convert back to int :)

Simply return this:
    return str(num) == (str(num))[::-1]
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = str(x)[::-1]
        if x < 0:
            return False
        elif x == int(reverse_x):
            return True
        else:
            return False
