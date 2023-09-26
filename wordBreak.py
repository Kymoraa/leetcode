"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Brute force: # Failed certain test cases
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            for i in range(len(s)):
                if word == s[:i+1]:
                    s = s.replace(word, '')
        return len(s) == 0
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)  # efficient lookup time
        memo = [False] * (len(s) + 1)
        memo[0] = True  # Base case

        for i in range(1, len(s) + 1):
            for j in range(i):
                if memo[j] and s[j:i] in wordSet:  # if the prefix and the substring s[j:i] are in the dictionary
                    memo[i] = True
                    break
        return memo[len(s)]
