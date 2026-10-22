class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        count = 0
        for start, end in intervals[1:]:
            endRes = res[-1][1]
            if start >= endRes:
                res.append([start, end])
            else:
                res[-1][1] = min(endRes, end)
                count += 1

        return count
        
        