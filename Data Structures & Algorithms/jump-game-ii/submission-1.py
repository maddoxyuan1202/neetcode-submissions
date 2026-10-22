class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        jump = 0

        for i in range(0, n-1):
            farthest = max(farthest, nums[i] + i)

            if i == end:
                end = farthest
                jump += 1


        return jump