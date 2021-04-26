"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

I placed the nums in a hashmap, and got the nums with the most count.
Looped through the sorted counts list to get the keys of these numbers in the hashmap
There is possibly a faster way to solve this. Also there is a bit of extra space needed here

"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        table = {}
        counts = []
        results = []

        if k == len(nums):
            return nums

        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1

        for x in table.values():
            counts.append(x)
        counts.sort(reverse=True)
        counts = counts[:k]

        for j in counts:
            elem = list(table.keys())[list(table.values()).index(j)]
            results.append(elem)
            table[elem] = None  # Set to None, in case an number has the same count as another. Avoids duplication

        return results
