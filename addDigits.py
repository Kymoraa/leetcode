"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example:
Input: num = 38
Output: 2

Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

N.B. I have seen solutions that use the mathematical approach.
They are def worth a look, as they are less costly than my solution below.

"""


class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        for i in str(num):
            result += int(i)

        if len(str(result)) != 1:
            result = self.addDigits(result)

        return result
