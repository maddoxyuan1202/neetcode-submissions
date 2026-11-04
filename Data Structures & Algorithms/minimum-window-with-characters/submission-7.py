class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        if s == t:
            return t
        countT = {}
        countS = {}

        l = 0
        res = ""
        minLen = float('inf')
        
        for i in range(n):
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        have, need = 0, len(countT)
        for r in range(m):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return res