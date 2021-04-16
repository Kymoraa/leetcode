"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Anagram = a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.

In this case one can simply make use of the inbuilt functions to sort the strings and compare. Return true if the sorted
strings are equal: return sorted(s) == sorted(t)

Though, if we need to expound on the algorithm, making use of a data structure might be best.
I had initially implemented it using a set but, sets have the property of only storing unique items thus strings like:
abb and aab would resolve to true.

Final implementation done using a hash map.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        items = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in items:
                items[i] += 1
            else:
                items[i] = 1

        for j in t:
            if j in items:
                items[j] -= 1
            else:
                return False

        for k in items:
            if items[k] != 0:
                return False
        return True
