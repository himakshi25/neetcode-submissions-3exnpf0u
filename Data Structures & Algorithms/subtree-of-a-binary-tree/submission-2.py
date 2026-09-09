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

        # if root is None:
        #     return False
        
        # left=self.isSubtree(root.left, subRoot)
        # right=self.isSubtree(root.right, subRoot)
        
        # ans = False
        # if root.val == subRoot.val:
        #     ans=self.sameTree(root, subRoot)
        
        # return ans or left or right
        self.s = ""
        self.inorder(subRoot)
        self.s2 =self.s
        self.s = ""
        self.inorder(root)
        self.s1 =self.s
        print(self.s1, self.s2)
        return self.s2 in self.s1



    def inorder(self,root):
        if root is None:
            self.s+='N' + ","
            return
        self.s+=str(root.val) + ","
        self.inorder(root.left)
        self.inorder(root.right)

        


        
        