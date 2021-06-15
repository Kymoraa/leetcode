"""
You're given strings jewels representing the types of stones that are jewels, & stones representing the stones you have.
Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".


Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

My brute force solution has the following stats:
Runtime: 28 ms, faster than 84.20% of Python3 online submissions for Jewels and Stones.
Memory Usage: 14 MB, less than 98.25% of Python3 online submissions for Jewels and Stones.

To-Do: Eliminate the nested for loops for a faster algorithm
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1
        return count
