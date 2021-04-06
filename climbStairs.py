"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2

Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

----
This is a problem that looks like the fibonacci sequence.
A recursive solution like the one below will work, however due to the many stack calls when a large n is executed,
we will run into a stack overflow error/time exeeded

class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 <= n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

Thus, there is need for a memoized or a bottom-up solution like the one below

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-up solution
        # Base case
        if 0 <= n <= 2:
            return n
        else:
            stairs = [0]*(n+1)
            stairs[1] = 1
            stairs[2] = 2

            for i in range(3, n+1):
                stairs[i] = stairs[i-1] + stairs[i-2]
            return stairs[n]