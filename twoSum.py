"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Difficulty level: Easy

# Solution 1
Have two loops through the array.
Sum the value from the first loop to the value from the second loop
If the sum == target, return the two indices
Time complexity: O(n^2)

# Solution 2
Make use of a dict data structure to store the difference between the target and the value at i
Check the dict if the value at i exists. This means that there is a number in the list which is equal to the target -
the value at i
Time complexity: O(n)

# Solution 3
Similar to solution two but eliminating the need for the two linear for loops

"""


class Solution:
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        output = []
        for i in range(n):
            for j in range(1, n):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)

        return output

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        memo = {}

        for i in range(n):
            val = target - nums[i]
            memo[i] = val

        for i in range(n):
            if nums[i] in memo:
                return [i, list(memo.keys())[list(memo.values()).index(nums[i])]]

    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        memo = {}

        for i in range(n):
            val = target - nums[i]
            if nums[i] in memo.keys():
                return [nums.index(val), i]
            else:
                memo[val] = nums[i]
