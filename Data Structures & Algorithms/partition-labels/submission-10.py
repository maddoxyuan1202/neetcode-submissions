class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indice = {}
        for i, v in enumerate(s):
            indice[v] = i
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, indice[c])

            if i == end:
                res.append(size)
                size = 0
        return res