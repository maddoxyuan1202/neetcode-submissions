class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        siSorted = sorted(s1)
        length = len(siSorted)
        l = 0
        r = length
        while r <= len(s2):
            if siSorted == sorted(s2[l:r]):
                return True
            else:
                l += 1
                r += 1
        return False
        
