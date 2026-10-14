class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, n = 0,1,len(prices)
        profit = 0
        while r < n:
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r

            r += 1
        return profit 