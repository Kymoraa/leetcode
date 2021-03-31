"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:

Input: nums = [2,2,1]
Output: 1

"""

# The best method I rely on is using a hashMap.
# Where by we loop through the input.
# Store the number at i as the key and the value as the number of times we have seen the key.
# Then print the key whose value is 1
# This of course makes use of extra space in the form of the hashMap O(n)


def singleNumberHash(nums):
    table = {}
    for i in nums:
        if i in table.keys():
            table[i] += 1
        else:
            table[i] = 1

    return list(table.keys())[list(table.values()).index(1)]


# A fewer lines method I just came across is using sets.
# Again, this makes use of extra space in the form of the set. O(n)


def singleNumberSet(nums):
    return 2 * sum(set(nums)) - sum(nums)


# Now the absolute best option to go with is using bit manipulation.
# There is no need for extra space. Constant space => O(1)
# XOR rules are:
# a ^ 0 = a
# a ^ a = 0
# a ^ a ^ c = c


def singleNumberBit(nums):
    a = 0
    for i in nums:
        a ^= i
    return a
