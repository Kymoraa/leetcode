"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        count = {}
        for word in s1.split(" "):
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        for word in s2.split(" "):
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        return [word for word in count if count[word] == 1]
