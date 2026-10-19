class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, height in enumerate(heights + [0]):
            while stack and height < heights[stack[-1]]:
                height_cal = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1

                else:
                     width = i

                maxArea = max(maxArea, height_cal * width)
            stack.append(i)
        
        return maxArea