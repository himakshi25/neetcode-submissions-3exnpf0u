# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_d=0

        self.diameterOfBT(root)

        return self.max_d
        
    def diameterOfBT(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        l= self.diameterOfBT(root.left)
        r= self.diameterOfBT(root.right)

        self.max_d = max(self.max_d,l+r)

        return 1+max(l,r)

        
        