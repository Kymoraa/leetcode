"""
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.


Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Stats:
Runtime: 71 ms, faster than 23.76% of Python3 online submissions for Counting Words With a Given Prefix.
Memory Usage: 14.1 MB, less than 32.17% of Python3 online submissions for Counting Words With a Given Prefix.
"""


class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        n = len(pref)
        count = 0
        for i in words:
            if i[:n] == pref:
                count += 1
        return count
