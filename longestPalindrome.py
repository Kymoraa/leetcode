"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        size = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j + 1]
                if sub_str == sub_str[::-1] and len(sub_str) > size:
                    ans = sub_str
                    size = len(sub_str)
        return ans
