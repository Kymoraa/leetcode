"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or
false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

"""

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        seen = set()
        for v in counts.values():
            if v in seen:
                return False
            else:
                seen.add(v)
        return True
