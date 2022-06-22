"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the
array.
Return the sum of all the unique elements of nums.


Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


Stats:
Runtime: 43 ms, faster than 71.17% of Python3 online submissions for Sum of Unique Elements.
Memory Usage: 13.9 MB, less than 53.90% of Python3 online submissions for Sum of Unique Elements.
"""


from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        sums = 0
        counts = dict(Counter(nums))
        for k, v in counts.items():
            if v == 1:
                sums += k
        return sums
