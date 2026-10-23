class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                weight = abs(x1 - x2) + abs(y1 - y2)

                graph[i].append((j, weight))
                graph[j].append((i, weight))

        
        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            res += cost
            for nei, wei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (wei, nei))

        return res