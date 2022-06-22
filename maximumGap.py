"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Stats:
Runtime: 1004 ms, faster than 91.81% of Python3 online submissions for Maximum Gap.
Memory Usage: 28 MB, less than 77.28% of Python3 online submissions for Maximum Gap.

PS. I've just realised that there is a time complexity caveat.
Due to the sort() method I have implemented, the solution will at the worst scenario have a logarithmic complexity i.e.
O(n log n) if either heap sort or merge sort is used.

Perhaps consider other forms of sorting in your implementation such as bucket sort

"""


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        max_gap = 0
        if len(nums) < 2:
            return max_gap
        else:
            nums.sort()
            for i in range(len(nums) - 1):
                curr_gap = nums[i + 1] - nums[i]
                max_gap = max(curr_gap, max_gap)
        return max_gap
