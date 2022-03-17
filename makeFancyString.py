"""
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.


Example 1:
Input: s = "leeetcode"
Output: "leetcode"

Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""

        for i in s:
            if len(res) >= 2 and res[-1] == i and res[-2] == i:
                continue
            res += i

        return res
