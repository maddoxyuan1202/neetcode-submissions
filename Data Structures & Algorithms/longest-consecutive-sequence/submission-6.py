
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedN = sorted(set(nums))

        count = 1
        res = 1

        for i in range(1, len(sortedN)):
            if sortedN[i] - sortedN[i - 1] == 1:
                count += 1
            else:
                count = 1

            res = max(res, count)

        return res