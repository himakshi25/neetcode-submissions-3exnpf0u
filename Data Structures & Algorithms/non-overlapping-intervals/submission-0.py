# sort by end value and use greedy approach, we need to always choose one whose end is less to minimise range.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        inters = sorted(intervals, key=lambda x: x[1])

        cur=inters[0]
        rem=0
        i=1
        while i<len(inters):
            if inters[i][0]>=cur[1]:
                cur=inters[i]
            else:
                rem+=1
            i+=1
        return rem
        