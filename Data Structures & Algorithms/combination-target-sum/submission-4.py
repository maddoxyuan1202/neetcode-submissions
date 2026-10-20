class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def allSub(start:int, total:int):
            if total == target:
                res.append(path.copy())
                return 

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                path.append(nums[i])
                allSub(i, total + nums[i])
                path.pop()

        allSub(0, 0)

        return res