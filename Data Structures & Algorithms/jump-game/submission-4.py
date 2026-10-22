class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        maxDis = 0
        n = len(nums)
        for i in range(n):
            if i > maxIdx:
                return False
            maxIdx = max(maxIdx, i + nums[i])

        return maxIdx >= n - 1
