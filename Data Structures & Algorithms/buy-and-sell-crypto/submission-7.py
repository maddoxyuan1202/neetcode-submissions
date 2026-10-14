class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        res = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = prices[r] - prices[l]
                res = max(res, maxP)
            else:
                l = r
            r += 1

        return res