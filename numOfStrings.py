"""
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring
in word.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

Runtime: 52 ms, faster than 49.80% of Python3 online submissions for Number of Strings That Appear as Substrings in
Word.
Memory Usage: 13.9 MB, less than 84.67% of Python3 online submissions for Number of Strings That Appear as Substrings
in Word.
"""


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count
