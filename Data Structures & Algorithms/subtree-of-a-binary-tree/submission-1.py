# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        
        return root.val == subRoot.val and self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        left=self.isSubtree(root.left, subRoot)
        right=self.isSubtree(root.right, subRoot)
        
        ans = False
        if root.val == subRoot.val:
            sub=subRoot
            ans=self.sameTree(root, sub)
            print(ans)
        
        return ans or left or right
        


        
        