"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Runtime: 58 ms, faster than 17.73% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.9 MB, less than 84.54% of Python3 online submissions for Backspace String Compare.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res = []
        for ch in s:
            if ch != "#":
                res.append(ch)
            else:
                if len(res) >= 1:  # to ensure it doesn't pop from an empty list if the elem at index 0 == #
                    res.pop()
        s = "".join(res)
        res.clear()

        for ch in t:
            if ch != "#":
                res.append(ch)
            else:
                if len(res) >= 1:
                    res.pop()
        t = "".join(res)

        if s == t:
            return True
        return False