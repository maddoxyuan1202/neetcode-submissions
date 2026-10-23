class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        # dijistra
        minHeap = [(0, k)]
        distance = {k: 0}
        while minHeap:
            dis, node = heapq.heappop(minHeap)
            if dis > distance[node]:
                continue
            for nei, weight in edges[node]:
                newDis = dis + weight

                if newDis < distance.get(nei, float('inf')):
                    distance[nei] = newDis
                    heapq.heappush(minHeap, (newDis, nei))


        if len(distance) != n:
            return -1

        return max(distance.values())

