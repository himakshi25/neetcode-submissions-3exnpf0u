# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: 
            return False
        slow = head
        fast = head
        while fast != None and slow != None:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                break;
            if slow == fast:
                return True
        return False