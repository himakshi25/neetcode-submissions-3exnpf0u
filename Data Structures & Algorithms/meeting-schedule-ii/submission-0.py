"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# l1->sorted start, l2->sorted end. we will fix a end pointer first and find how many meetings starting before this and doing ct++. stop where value l1>l2, now move pointer l2 and do ct--. showing that 1 meeting ended. likewise increment counter when you move l1 pointer and decrement when you move l2 and finding global max.


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)<2:
            return len(intervals)
        l1= sorted(intervals, key=lambda x: x.start)
        starts = [x.start for x in l1]
        l2= sorted(intervals, key=lambda x: x.end)
        ends = [x.end for x in l2]

        max_count = 0
        print (starts,ends)
        ct=0
        s=0
        e=0
        while e<len(ends):
            while s<len(starts) and ends[e]>starts[s]:
                ct+=1
                s+=1
            max_count = max(max_count,ct)
            e+=1
            ct-=1

        return max_count
        