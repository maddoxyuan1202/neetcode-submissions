class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i
        
        if target in indices:
            return indices[target]
        else:
            return -1
