class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        inf = float('inf')
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):

                dp[i] = min(
                    dp[i - coin] + 1,
                    dp[i]
                )

        return dp[amount] if dp[amount] != inf else -1