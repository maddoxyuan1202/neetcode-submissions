class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            if (first > second):
                heapq.heappush_max(stones, first-second)
        stones.append(0)
        return stones[0]