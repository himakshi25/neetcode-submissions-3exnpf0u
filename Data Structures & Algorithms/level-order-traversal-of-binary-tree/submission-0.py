# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        q=deque()
        q.append(root)
        q.append(None)

        ls = []
        while q:
            node = q.popleft()
            if node is None:
                ans.append(ls)
                ls=[]
                if q:
                    q.append(None)
            else:
                ls.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans

                



        