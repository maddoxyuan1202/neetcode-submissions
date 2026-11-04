class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res= []
        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            while heap and heap[0][1] < r - k + 1:
                heapq.heappop_max(heap)
            
            if r- k + 1 >= 0:
                res.append(heap[0][0])

        return res