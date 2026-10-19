class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights+[0]):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1]-1
                else:
                    width = i
                res = max(res, height * width)

            stack.append(i)
            
        return res