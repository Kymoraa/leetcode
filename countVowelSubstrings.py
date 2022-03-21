"""
A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u')
and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.


Example 1:
Input: word = "aeiouu"
Output: 2
1) aeiou
2) aeiouu

This is a brute force solution though. Complexity is O(n^2)

"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        s = set("aeiou")
        count = 0
        for i in range(len(word) - 4):
            for j in range(i + 5, len(word) + 1):
                if set(word[i:j]) == s:
                    count += 1

        return count
