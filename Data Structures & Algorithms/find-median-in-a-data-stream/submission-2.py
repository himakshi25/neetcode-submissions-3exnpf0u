# using two heap, max for first half and min for second half, to track mid elements for median, no need to maintain a sorted list.
import heapq
class MedianFinder:

    def __init__(self):
        self.mi=[]
        self.ma=[]

    def addNum(self, num: int) -> None:
        l1=len(self.ma)
        l2=len(self.mi)
        if l1 == 0:
            heapq.heappush(self.ma, -1*num)
        # elif l2 == 0:
        #     if num
        #     heapq.heappush(self.mi, num)
        elif num<-1*self.ma[0]:
            if l1>l2:
                heapq.heappush(self.mi, -1*heapq.heappushpop(self.ma,-1*num))
            else:
                heapq.heappush(self.ma, -1*num)
        else:
            heapq.heappush(self.mi, num)
            if len(self.mi)>l1:
                heapq.heappush(self.ma, -1*heapq.heappop(self.mi))   
        
        

    def findMedian(self) -> float:
        l1=len(self.ma)
        l2=len(self.mi)
        if l1==l2:
            return (self.mi[0]+(-1*self.ma[0]))/2
        return -1*self.ma[0]

        
        