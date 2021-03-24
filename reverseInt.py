"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverseInt(self, x: int) -> int:
        if x == 0:
            result = 0
        if x > 0:
            result = int(str(x)[::-1])  # string operation ro reverse the number converted to a string
        if x < 0:
            result = -1 * int(str(x * -1)[::-1])  # handle negatives

        # Take care of the 32-bit integer range
        min_range = -2 ** 31
        max_range = (2 ** 31) - 1

        if min_range < result < max_range:
            return result
        else:
            return 0
