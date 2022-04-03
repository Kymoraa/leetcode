"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false
otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        memo = {}
        for i in range(len(magazine)):
            if magazine[i] not in memo:
                memo[magazine[i]] = 1
            else:
                memo[magazine[i]] += 1
        for j in ransomNote:
            if j not in memo:
                return False
            if j in memo and memo[j] < 1:
                return False
            memo[j] -= 1
        return True
