class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i, num in enumerate(nums):
            nums_left = nums[:i] + nums[i+1:]
            indies = {}
            for i,n in enumerate(nums_left):
                indies[n] = i
            for i,n in enumerate(nums_left):
                diff = 0 - num - n
                if diff in indies and indies[diff] is not i:
                    res.append([num, nums_left[i], nums_left[indies[diff]]])
            
        unique = set()

        for triplet in res:
            unique.add(tuple(sorted(triplet)))

        res_unqiue = [list(triplet) for triplet in sorted(unique)]

        return res_unqiue
