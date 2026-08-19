# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        prev=head
        cur=prev.next
        prev.next=None

        while cur!= None:
            nextpt = cur.next
            cur.next=prev
            prev=cur
            cur=nextpt

        return prev

        
        