import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap=[]
        for p in points:
            dist = round(float(math.sqrt(p[0]**2 + p[1]**2)),5)
            pp = (-1*dist,p)
            if len(max_heap) == k:
                pt = heapq.heappop(max_heap)
                if dist>-1*pt[0]:
                    pp=pt
            heapq.heappush(max_heap, pp)

        return [item[1] for item in max_heap]



        