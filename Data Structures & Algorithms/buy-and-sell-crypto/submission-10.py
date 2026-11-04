class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        minPrice = float('inf')
        l = 0
        for r in range(n):
            if prices[r] < minPrice:
                minPrice = prices[r]
            maxProfit = max(maxProfit, prices[r] - minPrice)

        return maxProfit