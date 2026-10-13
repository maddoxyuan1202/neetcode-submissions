
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0

        for num in numSet:
            if (num - 1) not in numSet:
                lengest = 1 

                while (num + 1) in numSet:
                    num += 1
                    lengest += 1
                
                length = max(length, lengest)

        return length 