class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        hold = [0] * n
        cash = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            prev_cash = cash[i-2] if i >= 2 else 0

            hold[i] = max(
                hold[i-1],
                prev_cash - prices[i]
            )

            cash[i] = max(
                cash[i-1],
                hold[i-1] + prices[i]
            )

        return cash[-1]