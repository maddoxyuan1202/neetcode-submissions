class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indies = {}
        for i,n in enumerate(nums):
            indies[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in indies and indies[diff] is not i:
                return [i, indies[diff]]
        
        return []