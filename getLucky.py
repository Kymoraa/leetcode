"""
You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1,
'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits.
Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.



Example 1:

Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Stats
Runtime: 68 ms, faster than 15.26% of Python3 online submissions for Sum of Digits of String After Convert.
Memory Usage: 14 MB, less than 45.57% of Python3 online submissions for Sum of Digits of String After Convert.

Something new I picked from exploring this solution:
for _ in range(x)
"-" means: "we don't care about the iterator value, just that it should run some specific number of times"
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        conversions = dict()
        for index, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
            conversions[char] = (index + 1)

        chars = ""
        for i in s:
            for key, val in conversions.items():
                if i == key:
                    chars += str(val)
        for _ in range(k):
            output = 0
            for j in chars:
                output += int(j)
            chars = str(output)

        return int(chars)
