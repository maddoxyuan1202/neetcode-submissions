class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtracking(start: int):
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i+1)
                path.pop()

            return res
        
        res = backtracking(0)
        return res