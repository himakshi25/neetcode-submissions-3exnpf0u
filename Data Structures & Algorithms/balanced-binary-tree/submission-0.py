# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.answer=True

        self.isB(root)

        return self.answer


    def isB(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        l=self.isB(root.left)
        r=self.isB(root.right)

        if abs(l-r)>1:
            self.answer=False

        return 1+max(l,r)