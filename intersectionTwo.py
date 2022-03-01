"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any
order.



Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Runtime: 105 ms, faster than 13.42% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 57.72% of Python3 online submissions for Intersection of Two Arrays II.
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        for i in nums2:
            if i in nums1:
                output.append(i)
                nums1.remove(i)  # to refrain from referencing the same number twice
        return output
