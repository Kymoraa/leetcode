"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # converting the int list into a string, then into an integer for easy addition.
        # Then converting the result back into a list of integers
        digits = [str(i) for i in digits]
        digits = int(''.join(digits))
        digits = digits + 1
        return [int(x) for x in str(digits)]
