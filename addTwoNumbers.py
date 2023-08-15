"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

# Edge cases to consider
1. What if the LL are not of the same length/size?
2. If addition of values results in a two-digit number, maintain a carry value.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        result = ListNode()  # Create a dummy node to avoid the complexities of adding to a linked list. Space = O(n)
        current = result
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_val = v1 + v2 + carry
            carry = sum_val // 10
            sum_val = sum_val % 10

            current.next = ListNode(sum_val)

            # update the pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
