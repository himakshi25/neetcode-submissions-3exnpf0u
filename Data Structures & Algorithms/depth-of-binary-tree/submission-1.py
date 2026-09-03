# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.mD(root, 0, 0)

    def mD(self, root: Optional[TreeNode], max_ct, count) -> int:

        if root is None:
            return max(max_ct, count)
        
        count+=1

        l=self.mD(root.left, max_ct, count)
        r=self.mD(root.right, max_ct, count)

        return max(l,r)

        