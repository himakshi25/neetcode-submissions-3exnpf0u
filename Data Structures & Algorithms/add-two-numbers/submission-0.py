# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry=0
        ans=l1
        prev=None
        while l1 is not None and l2 is not None:
            add=l1.val+l2.val+carry
            carry=add//10
            l1.val=add%10
            prev=l1
            l1=l1.next
            l2=l2.next
        
        if l2 is not None:
            prev.next=l2
            while l2 is not None and carry>0:
                add=l2.val+carry
                carry=add//10
                l2.val=add%10
                prev=l2
                l2=l2.next
        else:
            while l1 is not None and carry>0:
                add=l1.val+carry
                carry=add//10
                l1.val=add%10
                prev=l1
                l1=l1.next
        
        if carry>0:
            newNode=ListNode(carry)
            prev.next=newNode
        
        return ans

                

        