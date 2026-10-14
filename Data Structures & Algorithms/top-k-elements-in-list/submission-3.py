class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        topF = sorted(count, key= lambda n:count[n], reverse= True) 

        return list(topF[:k])