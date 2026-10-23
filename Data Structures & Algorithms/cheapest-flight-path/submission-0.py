class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = float('inf')
        distance = [inf] * (n+1)
        distance[src] = 0

        for _ in range(k+1):
            temp = distance.copy()

            for u, v, w in flights:
                if distance[u] != inf and distance[u] + w < temp[v]:
                    temp[v] = distance[u] + w

            distance = temp


        if distance[dst] == inf:
            return -1

        return distance[dst]