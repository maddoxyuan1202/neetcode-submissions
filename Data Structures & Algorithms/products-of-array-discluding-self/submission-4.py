class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cunt = 1, 0
        indices = {}
        res = [0] * len(nums)

        for i,n in enumerate(nums):
            indices[n] = i
            if n == 0: zero_cunt +=1
            else:
                prod *= n

        if zero_cunt > 1:
            return res
        
        for i in range(len(nums)):
            if zero_cunt:
                res[indices[0]] = prod
            else:
                res[i] = prod // nums[i]

        return res