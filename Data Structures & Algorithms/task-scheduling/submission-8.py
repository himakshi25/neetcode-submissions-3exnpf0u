#  use max Priority Queue and put counters, then everytime pop n+1 and increase count and push only those whose counter non-zero
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        ans=0
        heap = []
        for k,v in mp.items():
            heapq.heappush(heap,(-1*v,k))

        while len(heap)>0:
            i=0
            pop=[]
            while len(heap)>0 and i<n+1:
                pop.append(heapq.heappop(heap))
                i+=1
            for v,k in pop:
                v=-1*v
                v-=1
                if v>0:
                    heapq.heappush(heap,(-1*v,k))
            if len(heap)==0:
                ans+=len(pop)
            else:
                ans+=n+1

        return ans
        