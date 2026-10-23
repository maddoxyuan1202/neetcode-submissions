class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        distance = {k: 0}

        while minHeap:
            dis, node = heapq.heappop(minHeap)
            if dis > distance[node]:
                continue

            for nei, d in graph[node]:
                newDist = d + dis
                if newDist < distance.get(nei, float('inf')):
                    distance[nei] = newDist
                    heapq.heappush(minHeap, (newDist, nei))

        if len(distance) != n:
            return -1

        return max(distance.values())     