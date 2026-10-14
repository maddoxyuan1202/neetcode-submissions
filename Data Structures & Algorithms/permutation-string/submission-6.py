class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = {}
        for ch in s1:
            countS1[ch] = countS1.get(ch, 0) + 1

        counttmp = {}
        for ch in s2[:len(s1)]:
            counttmp[ch] = counttmp.get(ch, 0) + 1
        
        if counttmp == countS1:
            return True

        l = 0
        r = len(s1)

        while r < len(s2):
            counttmp[s2[l]] -=1
            if counttmp[s2[l]] == 0:
                counttmp.pop(s2[l])

            counttmp[s2[r]] = counttmp.get(s2[r], 0) + 1

            l += 1
            r += 1
            if counttmp == countS1:
                return True

        return False
