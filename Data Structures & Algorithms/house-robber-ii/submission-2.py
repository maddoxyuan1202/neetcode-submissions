class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def helper(nums1):
            n = len(nums1)
            dp = [0] * (n+1)
            dp[0] = 0
            dp[1] = nums1[0]
            for i in range(2, n+1):
                dp[i] = max(
                    dp[i-1],
                    dp[i-2] + nums1[i-1]
                )
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
