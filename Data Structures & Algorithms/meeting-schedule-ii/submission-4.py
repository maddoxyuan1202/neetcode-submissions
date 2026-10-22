class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        s = 0
        e = 0
        rooms = 0
        res = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                res = max(res, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1

        return res