class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        target = sum(nums)//2

        n = len(nums)

        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, - 1, -1):
                if i >= num and dp[i - num]:
                    dp[i] = True

        
        return dp[target]

