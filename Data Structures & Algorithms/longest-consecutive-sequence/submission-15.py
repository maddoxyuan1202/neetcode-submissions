
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = {}
        res = 0

        for num in nums:
            if num in length:
                continue
            
            left = length.get((num-1), 0)
            right = length.get((num+1), 0)
            total = left + 1 + right 

            length[num] = total 
            length[num - left] = total
            length[num + right] = total

            res = max(total, res)

        return res