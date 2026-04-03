import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums) # O(n)
        pq = [] # keep only k items here
        for key, value in mp.items():  # O(n)
            heapq.heappush(pq,(value,key)) # O(logk)
            if(len(pq)>k):
                heapq.heappop(pq)

        return [x[1] for x in pq]