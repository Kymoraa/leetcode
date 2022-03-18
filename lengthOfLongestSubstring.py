"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        max_count = 0
        for ch in s:
            if ch in res:
                ind = res.index(ch)
                del res[0:ind + 1]
            res.append(ch)

            max_count = max(max_count, len(res))
        print(res)
        return max_count
