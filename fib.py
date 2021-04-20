"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

N.B. Be aware of the recursive calls that will lead to stack overflow error. Hence employ memoization like in the code
below or a bottom-up solution

"""


class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        if n <= 0:
            return 0
        if n<= 2:
            return 1
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib(n-1) + self.fib(n-2)
            return memo[n]
