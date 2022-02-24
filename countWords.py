"""
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the
two arrays.

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2

Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.

Thus, there are 2 strings that appear exactly once in each of the two arrays.
"""
from collections import Counter


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)
        res = 0

        for word in counter1:
            if counter1[word] > 1:
                continue
            if word not in counter2:
                continue
            if counter2[word] == 1:
                res += 1
        return res
