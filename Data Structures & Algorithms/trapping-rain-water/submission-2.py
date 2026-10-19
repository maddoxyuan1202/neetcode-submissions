class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i, n in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack.pop()]

                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(left, right) - mid
                    w = i - stack[-1] -1 
                    res += h*w

            stack.append(i)

        return res