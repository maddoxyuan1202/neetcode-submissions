class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        numSet = set()
        numList = set()

        def dfs(start:int):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)

        seen = set()
        unique = []

        for item in res:
            key = tuple(sorted(item))

            if key not in seen:
                seen.add(key)
                unique.append(item)
        


        return unique
