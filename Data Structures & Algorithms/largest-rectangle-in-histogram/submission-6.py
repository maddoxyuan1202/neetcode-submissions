class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[i] <= heights[stack[-1]]):
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                res = max(res, height * width)
            stack.append(i)
        return res
                