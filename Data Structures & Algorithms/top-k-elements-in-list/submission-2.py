class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = defaultdict(int)
        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1
        
        res = sorted(numDict, key=lambda n: numDict[n], reverse=True)

        return res[:k]