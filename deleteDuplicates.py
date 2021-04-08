"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode):
        if head is None:
            return head

        temp = head

        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
                continue
            head = head.next
        return temp
