import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums) # O(n)
        pq = []
        out = []
        for key, value in mp.items():  # O(n)
            heapq.heappush(pq,(-value,key)) # O(logk)
        
        for i in range(k):
            out.append(heapq.heappop(pq)[1])

        return out
        