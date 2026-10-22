class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        size = 0
        farthest = 0

        res = []

        for i, v in enumerate (s):
            lastIndex[v] = i

        for i,  v in enumerate(s):
            farthest = max(farthest, lastIndex[v])
            size += 1
            if (i == farthest):
                res.append(size)
                size = 0
        return res
