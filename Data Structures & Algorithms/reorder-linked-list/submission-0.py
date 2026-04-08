# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        hm = {}
        cur = head
        while cur!= None:
            hm[l] = cur
            l+=1
            cur = cur.next
        #print(f"{l}  {hm} ")
        new = head
        even = -1
        odd = 1
        i=1
        while i<l:
            #print(f"{even} {odd} {(i+1)%2}")
            if (i+1)%2 == 0: # even position
                new.next = hm[l+even]
                even-=1
            else:
                new.next = hm[odd]
                odd+=1
            #print(new.next.val)
            new = new.next
            
            i+=1
        new.next = None

        