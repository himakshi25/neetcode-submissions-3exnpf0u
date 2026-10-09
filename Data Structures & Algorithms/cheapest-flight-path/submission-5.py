from collections import defaultdict,deque
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj=defaultdict(list)
        for s,d,p in flights:
            adj[s].append((d,p))

        min_price=[float('inf')]*n
        min_price[src]=0
        q=deque()
        q.append(src)
        nf=1
        while nf<=k+1:
            prev_price=min_price.copy()
            for i in range(len(q)):
                ind = q.popleft()
                for d,p in adj[ind]:
                    if prev_price[ind]+p<min_price[d]:
                        min_price[d]=prev_price[ind]+p
                        q.append(d)
                    #print(nf, prev_price)
            nf+=1
            #print(min_price)


        return min_price[dst] if min_price[dst] != float('inf') else -1
        