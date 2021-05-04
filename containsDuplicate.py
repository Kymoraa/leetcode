"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false

Used a set DS to store all the values that I had already seen. Thus, if we come across that value again we return True.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
