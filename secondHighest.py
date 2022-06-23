"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.

Stats:
Runtime: 91 ms, faster than 6.79% of Python3 online submissions for Second Largest Digit in a String.
Memory Usage: 13.8 MB, less than 97.16% of Python3 online submissions for Second Largest Digit in a String.
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        digits = set()
        for i in s:
            if i in nums:
                digits.add(int(i))
        if len(digits) < 2:
            return -1
        return sorted(list(digits))[-2]
