
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0

        for num in nums:
            if (num -1) not in numSet:
                longest = 1
                while (num + longest) in numSet:
                    longest += 1

                length = max(length, longest) 

        return length