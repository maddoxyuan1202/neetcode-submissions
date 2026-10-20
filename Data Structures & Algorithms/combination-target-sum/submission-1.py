class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def addToTarget(start: int, cur: List[lint], total:int):
            if (total == target):
                res.append(cur.copy())
                return

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    break
                cur.append(nums[i])
                
                addToTarget(i, cur, total+nums[i])

                cur.pop()

        addToTarget(0, [], 0)

        return res
        
            
