"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

I have implemented this using a hash map where the nums are the keys and the value is how many times the number appears
Note, this uses additional auxiliary space. Thus space complexity will be O(n) where as time will be linear O(n)


Follow-up: Could you solve the problem in linear time and in O(1) space?

Maybe consider sorting the array...
nums.sort()
        return nums[len(nums)//2]

Time complexity : O(n log n)
Space complexity : O(1)

This increases the time complexity to logarithmic though due to the sorting cost.

"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        table = {}
        n = len(nums) // 2

        for i in nums:
            if i in table.keys():
                table[i] += 1
            else:
                table[i] = 1

        for i in table.values():
            if i > n:
                return list(table.keys())[list(table.values()).index(i)]
