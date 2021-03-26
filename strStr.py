"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Base cases
        if (needle == haystack) or len(needle) == 0:
            return 0
        elif (needle in haystack) and len(haystack) > 0:
            return haystack.index(needle)
        else:
            return -1

