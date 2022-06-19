"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""
import math
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        memo = Counter(text)
        if 'o' in memo:
            if memo['o'] > 1:
                memo['o'] /= 2
            elif memo['o'] == 1:
                return 0
        if 'l' in memo:
            if memo['l'] > 1:
                memo['l'] /= 2
            elif memo['l'] == 1:
                return 0
        return math.floor(min([memo[ch] for ch in 'balloon']))
