"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

Used a set to solve the problem.
Traverse LL1 and store the nodes in the set
Traverse LL2 and check for the presence of the nodes in the set
If present, then return the node. Else return null.

Notice that this implementation makes use of an additional data structure hence increasing the space complexity yo O(n)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        nodes = set()

        while headA is not None:
            nodes.add(headA)
            headA = headA.next

        while headB is not None:
            if headB in nodes:
                return headB
            headB = headB.next
        return None
