# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        s=head
        f=head.next.next
        while f is not None and f.next is not None:
            if s.val == f.val:
                return True
            s=s.next
            f=f.next.next

        return False
        