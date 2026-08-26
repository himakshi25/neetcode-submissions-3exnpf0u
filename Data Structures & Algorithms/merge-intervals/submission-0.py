# 1. i used heap and sorted by end times, pop and compare their start times. this gives unordererd output.
# 2. best is using sorting first and then merging interval in 1 pass. this will give outpur sorted by start time.
import heapq
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_heap = []
        res=[]
        for interval in intervals:
            heapq.heappush(max_heap,[-1*interval[1], interval[0]])
        
        cur = heapq.heappop(max_heap)
        cur[0]=cur[0]*-1
        print(cur)
        while max_heap:
            sec = heapq.heappop(max_heap)
            sec[0]*=-1
            if sec[0]>=cur[1]:
                cur[1]= min(cur[1], sec[1])
            else:
                res.append([cur[1],cur[0]])
                cur=sec
            print(cur)
        res.append([cur[1],cur[0]])     
        return res