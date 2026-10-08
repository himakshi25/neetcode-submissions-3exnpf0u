from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans=-1
        adj=defaultdict(list)
        for e in times:
            adj[e[0]].append((e[1],e[2]))
        #print(adj)
        v=[float('inf')]*(n+1)
        v[0]=0
        #print(v)
        v[k]=0
        pq=[]
        heapq.heappush(pq, (100000,k))
        while pq:
            pop=heapq.heappop(pq)
            s=pop[1]
            for n in adj[s]:
                dist=v[s]+n[1]
                if dist<v[n[0]]:
                    v[n[0]]=dist
                    heapq.heappush(pq, (dist,n[0]))
            #print(pop, pq)
        #print(v)
        return -1 if float('inf') in v else max(v)

        