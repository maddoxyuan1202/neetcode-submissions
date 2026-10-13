class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []
        for num in nums:
            freq[num] += 1
        
        indice_return = sorted(freq, key = lambda n : freq[n], reverse=True)

        return indice_return[:k]