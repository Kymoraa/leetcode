"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}
        for i in range(len(s)):
            if s[i] not in memo:
                memo[s[i]] = 1
            else:
                memo[s[i]] += 1
        for k, v in memo.items():
            if v == 1:
                return s.index(k)
        return -1
