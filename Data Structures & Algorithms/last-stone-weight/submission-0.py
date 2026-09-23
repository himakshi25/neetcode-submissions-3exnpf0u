import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for st in stones:
            heapq.heappush(max_heap, -1*st)
        

        while len(max_heap)>1:
            num1 = -heapq.heappop(max_heap)
            num2 = -heapq.heappop(max_heap)
            print(num1,num2)

            if num1 != num2:
                heapq.heappush(max_heap, -1*(num1-num2))
        
        return -heapq.heappop(max_heap) if len(max_heap)>0 else  0



        