"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5

Input: s = " "
Output: 0

Input: s = "a b    "
Output: 1
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split(" ")
        n = len(result)
        for i in range(n-1, -1, -1):
            if len(result[i]) != 0:
                return len(result[i])
        return 0
