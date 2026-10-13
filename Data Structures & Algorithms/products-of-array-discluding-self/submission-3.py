class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cunt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cunt += 1

        if zero_cunt > 1: return [0]* len(nums)
        res = [0]* len(nums)

        for i,  n in enumerate(nums):
            if zero_cunt > 0:
                if n == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // n 


        
        return res