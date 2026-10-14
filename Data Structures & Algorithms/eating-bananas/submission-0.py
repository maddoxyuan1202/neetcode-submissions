class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        minRate = 1

        while maxRate >= minRate:
            totalTime = 0
            midRate = (maxRate + minRate) // 2

            for i in range(len(piles)):
                totalTime += math.ceil(piles[i] / midRate)

            if totalTime > h:
                minRate = midRate + 1
            else:
                maxRate = midRate - 1

        return minRate