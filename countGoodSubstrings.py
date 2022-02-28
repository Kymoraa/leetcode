"""
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.


> Example 1:
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".

> Example 2:
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

* My solution*
Implemented a window of length 3
Add the chars in that window to a set and check on the length
If the length ==3, it means the substring is good as no chars are repeated

Runtime: 49 ms, faster than 45.29% of Python3 online submissions for Substrings of Size Three with Distinct
Characters. Memory Usage: 13.8 MB, less than 79.59% of Python3 online submissions for Substrings of Size Three with
Distinct Characters.

"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            sub_str = set(s[i:3 + i])
            if len(sub_str) == 3:
                count += 1
        return count
