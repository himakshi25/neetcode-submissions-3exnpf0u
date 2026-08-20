# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n==1:
            return None
        d=ListNode()
        d.next=head
        s,f=d,d

        for i in range(n):
            f=f.next

        while f.next is not None:
            s=s.next
            f=f.next
        
        remove=s.next
        s.next=s.next.next
        remove=None
        return d.next
        