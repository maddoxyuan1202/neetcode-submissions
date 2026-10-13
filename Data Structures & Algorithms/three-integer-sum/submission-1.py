class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()

        for i in range(len(nums)):
            index1 = i + 1
            index2 = len(nums) - 1

            while index1 < index2:
                total = nums[i] + nums[index1] + nums[index2]

                if total == 0:
                    triplet = (
                        nums[i],
                        nums[index1],
                        nums[index2]
                    )

                    if triplet not in seen:
                        res.append(list(triplet))
                        seen.add(triplet)

                    index1 += 1
                    index2 -= 1

                elif total > 0:
                    index2 -= 1

                else:
                    index1 += 1

        return res