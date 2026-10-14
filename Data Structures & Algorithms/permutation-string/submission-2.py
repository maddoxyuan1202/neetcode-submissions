class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        siSorted = sorted(list(s1))
        length = len(siSorted)
        l = 0
        r = length
        while r <= len(s2):
            if siSorted == sorted(list(s2[l:r:1])):
                return True
            else:
                l += 1
                r += 1
        return False
        
