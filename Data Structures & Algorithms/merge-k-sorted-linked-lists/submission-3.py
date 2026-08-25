# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap=[]
        ct=0
        head=ListNode()
        cur=head
        for node in lists:
            if node is not None:
                ct+=1
                heapq.heappush(heap,(node.val,ct,node))
        
        while(heap):
            val,n,node = heapq.heappop(heap)
            cur.next=node
            cur=cur.next
            node=node.next
            if node:
                ct+=1
                heapq.heappush(heap,(node.val,ct,node))
        return head.next

        