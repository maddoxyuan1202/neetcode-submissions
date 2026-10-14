class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(numbers):
            indices[n] = i
        res = []
        l = 0
        r = len(numbers) -1 

        while r > l:
            if numbers[r] + numbers[l] < target:
                l += 1
            elif numbers[r] + numbers[l] > target:
                r -= 1
            else:
                res = [l+1, r+1]
                l += 1
                r -= 1

        return res
        