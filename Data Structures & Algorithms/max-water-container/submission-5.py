class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        maxArea = 0
        while l < r:
            targetArea = (r-l) * min(heights[l], heights[r])
            maxArea = max(maxArea, targetArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea
                