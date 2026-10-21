class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify_max(minHeap)
        while len(minHeap) > k:
            heapq.heappop_max(minHeap)

        for item in minHeap:
            res.append([item[1], item[2]])

        return res

        