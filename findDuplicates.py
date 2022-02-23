"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears
once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
"""

"""
The below is the solution I could think of first. But, memory-wise, it is not the best solution to go with, as we are
using two DS for the operation.

*The stats for the submission*
Runtime: 558 ms, faster than 36.21% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 23.5 MB, less than 8.65% of Python3 online submissions for Find All Duplicates in an Array.
"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        memo = set()
        output = []
        for i in range(len(nums)):
            if nums[i] in memo:
                output.append(nums[i])
            else:
                memo.add(nums[i])
        return output


"""
I came across this other solution which is probably more memory efficient

* Since the element can appear once or twice, loop through all the elements of the list. 
Every time you go to an element, turn the value at the index of that element to negative to mark that you have seen this 
element once.

First scenarios: In every element (i), check the value of the element at index (i), if it is negative -> Then it has 
appeared before -> Then it is what we are looking for.
Second scenarios: If the value of the element at index (i) is still positive -> Then it is the first time we meet it -> 
Turn it to negative and continue.                                                                                                                                                                                                    
"""


class Solution:
    def findDuplicates2(self, nums: list[int]) -> list[int]:
        answers = []

        for num in nums:
            if nums[abs(num) - 1] < 0:
                answers.append(abs(num))
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]

        return answers
