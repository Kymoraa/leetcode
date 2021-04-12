"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Solved using:
Floyd’s Cycle-Finding Algorithm
> Traverse linked list using two pointers.
> Move one pointer(slow_p) by one and another pointer(fast_p) by two.
> If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t
have a loop.

Complexity Analysis:

Time complexity: O(n). Only one traversal of the loop is needed.
Auxiliary Space:O(1). There is no space required.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        pointer1 = head
        pointer2 = head

        while pointer1 and pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return True

        return False
