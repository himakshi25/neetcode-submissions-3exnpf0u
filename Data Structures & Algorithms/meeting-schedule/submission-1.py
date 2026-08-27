"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if (len(intervals)==0):
            return True
        inter=sorted(intervals, key=lambda x: x.start)
        pe=inter[0].end
        for i in inter[1:]:
            if pe>i.start:
                return False
            pe=i.end
        
        return True

