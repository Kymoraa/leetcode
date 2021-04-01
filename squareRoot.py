"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Python has an inbuilt square root method sqrt(x) so you can just return int(sqrt(x)

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        res = x**0.5
        return int(res)
