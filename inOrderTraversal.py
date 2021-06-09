"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]

NB. inOrder traversal is: leftNode, root, rightNode
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        else:
            return self.inOrderTraversal(root.left) + [root.val] + self.inOrderTraversal(root.right)
