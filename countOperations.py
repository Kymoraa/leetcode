"""
Return the number of operations required to make either num1 = 0 or num2 = 0.

Example 1:
Input: num1 = 2, num2 = 3
Output: 3
Explanation:
- Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.

My Stats*
Runtime: 594 ms, faster than 5.01% of Python3 online submissions for Count Operations to Obtain Zero.
Memory Usage: 14.3 MB, less than 7.34% of Python3 online submissions for Count Operations to Obtain Zero.
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        res = 1000

        while res > 0:
            if num1 == 0 or num2 == 0:
                count = 0
                break
            if num2 > num1:
                num1, num2 = num2, num1
            res = num1 - num2
            print(num2)
            num1 = res
            count += 1
        return count
