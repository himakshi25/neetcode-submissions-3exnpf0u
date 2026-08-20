# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# find midlle element using 2 pointer and then reverse other half making as list2 and then do list1-list2-list1 ordering
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        s=head
        f=head
        l1=head
        c=0
        while f is not None and f.next is not None:
            s=s.next
            f=f.next.next
            c+=1
        
        if f is None:
            l2=s
        else:
            l2=s.next
        
        # reverse l2
        p=l2
        cur=p.next
        while cur is not None:
            n=cur.next
            cur.next=p
            p=cur
            cur=n
        l2=p
        d=ListNode()
        head=d
        i=1
        while i<=c*2:
            if i%2==0:
                d.next=l2
                l2=l2.next       
            else:
                d.next=l1
                l1=l1.next
            d=d.next
            i+=1
        
        if f is not None:
            d.next=l1
            d=d.next
        d.next=None
