# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.mD(root, 0)

    def mD(self, root: Optional[TreeNode], count) -> int:

        if root is None:
            return count
        
        count+=1

        l=self.mD(root.left, count)
        r=self.mD(root.right, count)

        return max(l,r)

        