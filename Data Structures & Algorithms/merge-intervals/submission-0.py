class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            endRes = res[-1][1]

            if start > endRes :
                res.append([start, end])
            else:
                res[-1][1] = max(endRes, end)

        return res