"""
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is
a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a
prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

Example 1:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

Runtime: 60 ms, faster than 9.10% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in
a Sentence.
Memory Usage: 13.8 MB, less than 77.78% of Python3 online submissions for Check If a Word Occurs As a
Prefix of Any Word in a Sentence.
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        lst_sentence = sentence.split(" ")
        for i in lst_sentence:
            if i[:n] == searchWord:
                return lst_sentence.index(i) + 1

        return -1
