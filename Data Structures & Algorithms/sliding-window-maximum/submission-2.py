class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res= []
        heap = []
        for r in range(n):
            heapq.heappush_max(heap, (nums[r], r))
            while heap and heap[0][1] <= r-k:
                heapq.heappop_max(heap)

            if r - k + 1>= 0:
                res.append(heap[0][0])
        
        return res
