class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            seen[sortedS].append(s)
        
        return list(seen.values())