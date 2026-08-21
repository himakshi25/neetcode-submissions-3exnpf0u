# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head.next is None or left == right:
            return head

        ct=1
        d=ListNode()
        d.next=head
        head=d

        while ct < left:
            head=head.next
            ct+=1

        print(ct)

        s=head
        p=s.next
        c=p.next

        print(s.val,p.val,c.val)

        while(ct<right):
            print(c.val, ct)
            n=c.next
            c.next=p
            p=c
            c=n
            ct+=1
        
        print(p.val)

        r=s.next
        s.next=p
        r.next=c

        return d.next

        