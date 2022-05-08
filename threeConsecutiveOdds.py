"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array.
Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Stats:
Runtime: 47 ms, faster than 86.98% of Python3 online submissions for Three Consecutive Odds.
Memory Usage: 13.9 MB, less than 57.64% of Python3 online submissions for Three Consecutive Odds.
"""


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i]%2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False
