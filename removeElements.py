"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.

Example:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        while head and head.val == val:
            head = head.next

        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head
