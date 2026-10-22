"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        res = False
        if not intervals:
            return True
        first = intervals[0]

        for interval in intervals[1:]:
            if interval.start >= first.end:
                first = interval
            else:
                return False

        return True
            