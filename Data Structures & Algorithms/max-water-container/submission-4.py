class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        indices = {}
        res = 0
        l, r = 0, len(heights) -1 

        while l < r:
            maxArea = min(heights[l], heights[r]) * (r - l)
            res = max(res, maxArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return res
            