class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        for ch in s1:
            countS1[ch] = countS1.get(ch, 0) + 1
        l = 0
        r = len(s1)
        while r <= len(s2):
            counttmp = {}
            for ch in s2[l:r]:
                counttmp[ch] = counttmp.get(ch, 0) + 1
            if (counttmp == countS1):
                return True
            else:
                r +=1
                l +=1
        return False