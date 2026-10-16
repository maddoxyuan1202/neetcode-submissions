class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                numSet.remove(num)
        
        return not len(numSet)