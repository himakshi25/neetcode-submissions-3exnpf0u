# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def inorder(self, root, k):
    #     if root is None or self.ans is not None :
    #         return
        
    #     self.inorder(root.left,k)
    #     self.count+=1
    #     if k == self.count:
    #         self.ans=root.val
    #     self.inorder(root.right,k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # self.count=0
        # self.ans=None
        # self.inorder(root,k)
        # return self.ans

        st=[]
        count=0
        st.append(root)
        while st:
            while st[-1] and st[-1].left:
                print(st[-1].val)
                st.append(st[-1].left)
            while st and st[-1].right is None:
                count+=1
                if count == k:
                    return st[-1].val
                st.pop()
            if st:
                top=st[-1]
                st.pop()
                count+=1
                if count == k:
                    return top.val
                if top.right:
                    st.append(top.right)
        



        