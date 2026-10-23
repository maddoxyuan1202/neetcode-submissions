class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        distance = {k: 0}
        minHeap = [(0, k)]

        while minHeap:
            dis, node = heapq.heappop(minHeap)
            if dis > distance[node]:
                continue
            for nei, weight in edges[node]:
                newDist = dis + weight

                if newDist < distance.get(nei, float('inf')):
                    distance[nei] = newDist
                    heapq.heappush(minHeap, (newDist, nei))

        if len(distance) != n:
            return -1
        return max(distance.values())
