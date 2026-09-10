# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return ans
        
        q=deque()
        q.append(root)
        level_size=len(q)

        while level_size != 0:
            node=q.popleft()
            level_size-=1
        
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            if level_size==0:
                ans.append(node.val)
                level_size=len(q)
        return ans
        