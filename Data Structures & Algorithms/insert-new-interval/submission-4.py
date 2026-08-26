class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        resInt=[]
        if len(intervals)==0:
            resInt.append(newInterval)
            return resInt
        eIn=-1
        i=0
        while i<len(intervals):
            if newInterval[0] <= intervals[i][1]:
                break;
            resInt.append(intervals[i])
            i+=1
        if i<len(intervals):
            ms = min(intervals[i][0], newInterval[0])
        else:
            ms=newInterval[0]
        while i<len(intervals):
            if newInterval[1] < intervals[i][0]:
                break;
            i+=1
        if i-1>=0:
            me= max(newInterval[1],intervals[i-1][1])
        else:
            me=newInterval[1]
        resInt.append([ms,me])
        
        while i<len(intervals):
            resInt.append(intervals[i])
            i+=1

        return resInt
        