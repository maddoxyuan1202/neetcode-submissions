class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaMax = 0
        i, j = 0, len(heights) - 1
        while i < j:
            area = (j - i) * min(heights[j], heights[i])
            areaMax = max(area, areaMax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return areaMax