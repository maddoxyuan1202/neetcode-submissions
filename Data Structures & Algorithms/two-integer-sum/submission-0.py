class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)

        for index1 in range(lens):
            for index2 in range(index1+1, lens):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
                


            