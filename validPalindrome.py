"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Join the alphanumeric chars in a string removing all spaces and special characters.
        # Then convert to lower case
        # compare the original string with the reversed string
        s = ''.join(e for e in s if e.isalnum()).lower()
        if s == s[::-1]:
            return True
        else:
            return False
