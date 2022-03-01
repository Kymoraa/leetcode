"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
be unique and you may return the result in any order.


*My solution
Convert both lists to sets so as to maintain only unique nums
Loop through the smaller set to find similar nums in the larger set
Add those to the results set
Return set as list

Runtime: 54 ms, faster than 74.43% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.1 MB, less than 62.36% of Python3 online submissions for Intersection of Two Arrays.

"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = set()
        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) < len(nums2):
            nums2, nums1 = nums1, nums2

        for i in nums2:
            if i in nums1:
                ans.add(i)

        return list(ans)