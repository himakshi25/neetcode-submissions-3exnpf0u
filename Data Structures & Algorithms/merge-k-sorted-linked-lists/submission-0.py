# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode(-1)
        cur = res
        i = 0
        if len(lists) == 0 or lists[0] == None: return None
        for ls in lists:
            heapq.heappush(heap, (ls.val,i,ls))
            i+=1
        while len(heap) != 0:
            minNode = heapq.heappop(heap)[2]
            minNodeNext = minNode.next
            if minNodeNext != None:
                heapq.heappush(heap, (minNodeNext.val,i,minNodeNext))
                i+=1
            minNode.next = None
            cur.next = minNode
            cur = cur.next

        return res.next
        