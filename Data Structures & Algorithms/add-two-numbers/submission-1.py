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
        
        remain = l2 if l2 is not None else l1
        prev.next=remain
        while remain is not None and carry>0:
            add=remain.val+carry
            carry=add//10
            remain.val=add%10
            prev=remain
            remain=remain.next
        
        if carry>0:
            newNode=ListNode(carry)
            prev.next=newNode
        
        return ans

                

        