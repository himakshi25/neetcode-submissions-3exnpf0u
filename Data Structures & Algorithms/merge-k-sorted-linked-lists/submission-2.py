# Divide and conquer for space O(logk) without using heap
# lists = [L1, L2, L3, L4, L5, L6]

# Step 1: Pair merge
#   merge(L1, L2) → R1
#   merge(L3, L4) → R2
#   merge(L5, L6) → R3
#   Result: [R1, R2, R3]

# Step 2: Pair merge again
#   merge(R1, R2) → R4
#   merge(R3, None) → R5 (only one left)
#   Result: [R4, R5]

# Step 3: Final merge
#   merge(R4, R5) → Final result

import heapq
class Solution:  
    def mergelists(self, left: Optional[ListNode], right: Optional[ListNode]):
        head = ListNode(-1)
        cur = head
        while left!=None and right != None:
            if left.val<right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left==None:
            cur.next =right
        else:
            cur.next =left
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergelists(left, right)

        