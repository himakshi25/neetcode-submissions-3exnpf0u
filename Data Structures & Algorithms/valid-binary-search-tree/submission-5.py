# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bst(self, root):

        if root is None:
            return

        self.bst(root.left)
        if self.prev>=root.val:
            self.ans = False
        self.prev=root.val
        self.bst(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.prev=float('-inf')
        self.bst(root)
        return self.ans
        

        