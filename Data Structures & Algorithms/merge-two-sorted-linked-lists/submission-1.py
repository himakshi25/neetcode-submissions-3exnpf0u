# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return None
        
        d=ListNode()
        head=d
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                d.next=list1
                list1=list1.next
                #list1.next=None
            else:
                d.next=list2
                list2=list2.next
                #list2.next=None
            d=d.next
        if list1 is not None:
            d.next=list1
        if list2 is not None:
            d.next=list2
        return head.next

        