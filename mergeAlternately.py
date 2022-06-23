"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Stats:
Runtime: 53 ms, faster than 30.31% of Python3 online submissions for Merge Strings Alternately.
Memory Usage: 13.8 MB, less than 98.36% of Python3 online submissions for Merge Strings Alternately.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = ''
        while i < len(word1) and j < len(word2):
            res += word1[i]
            i += 1
            res += word2[j]
            j += 1

        while i < len(word1):
            res += word1[i]
            i += 1

        while j < len(word2):
            res += word2[j]
            j += 1
        return res
