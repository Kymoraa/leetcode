"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Of course in Python there is an inbuilt function to convert a string to lower case in one line;
Simply, return string.lower()
However, I doubt this simple one liner will suffice for an algorithm question

I did an implementation using a dict of alphabets.

The performance of the algorithm:
Runtime: 24 ms, faster than 91.90% of Python3 online submissions for To Lower Case.
Memory Usage: 14.3 MB, less than 38.71% of Python3 online submissions for To Lower

"""


class Solution:
    def toLowerCase(self, string: str) -> str:
        alphabets = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H", "i": "I", "j": "J",
                     "l": "L", "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U",
                     "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z"}

        result = ""
        for char in string:
            if char in alphabets.values():
                x = list(alphabets.keys())[list(alphabets.values()).index(char)]
                result += x
            else:
                result += char
        return result
