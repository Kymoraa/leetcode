"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than
25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1

Runtime: 101 ms, faster than 85.46% of Python3 online submissions for Element Appearing More Than 25% In Sorted Array.
Memory Usage: 15.6 MB, less than 42.22% of Python3 online submissions for Element Appearing More Than 25% In Sorted
Array.

// I realise there are probably better solutions. Like this one which i've just come across.
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        per = len(arr)//4
        for i in arr:
            occ = arr.count(i)
            if occ > per:
                return i
"""

from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        occ = (25 * len(arr)) // 100
        memo = Counter(arr)
        val = max([memo[i] for i in memo])
        if val > occ:
            return list(memo.keys())[list(memo.values()).index(val)]
