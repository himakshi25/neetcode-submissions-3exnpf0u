# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, k):
        if root is None:
            return
        
        self.inorder(root.left,k)
        self.count+=1
        if k == self.count:
            self.ans=root.val
        self.inorder(root.right,k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        self.ans=0
        self.inorder(root,k)
        return self.ans

        