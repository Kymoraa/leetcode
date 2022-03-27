"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half
and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Runtime: 49 ms, faster than 59.15% of Python3 online submissions for Determine if String Halves Are Alike.
Memory Usage: 13.9 MB, less than 40.11% of Python3 online submissions for Determine if String Halves Are Alike.

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        vowels = set('aeiou')

        for i in a:
            if i in vowels:
                a = a.replace(i, '')
        for j in b:
            if j in vowels:
                b = b.replace(j, '')
        return len(a) == len(b)
