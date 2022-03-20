"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at
the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3
(inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Runtime: 44 ms, faster than 51.44% of Python3 online submissions for Reverse Prefix of Word.
Memory Usage: 13.8 MB, less than 73.29% of Python3 online submissions for Reverse Prefix of Word.
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        if ch not in word:
            return ''.join(word)
        else:
            idx = word.index(ch)
            word1 = word[:idx+1]
            word2 = word[idx+1:]
            word1.reverse()
            res = word1 + word2
            return ''.join(res)
