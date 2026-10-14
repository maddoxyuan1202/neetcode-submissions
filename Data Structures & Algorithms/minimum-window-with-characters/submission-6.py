class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        countS = {}
        countT = {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        have = 0
        need = len(countT)

        l = 0
        minLen = float("inf")
        start = 0

        for r in range(len(s)):
            ch = s[r]
            countS[ch] = countS.get(ch, 0) + 1

            if ch in countT and countS[ch] == countT[ch]:
                have += 1

            while have == need:
                windowLen = r - l + 1

                if windowLen < minLen:
                    minLen = windowLen
                    start = l

                leftChar = s[l]
                countS[leftChar] -= 1

                if leftChar in countT and countS[leftChar] < countT[leftChar]:
                    have -= 1

                l += 1

        if minLen == float("inf"):
            return ""

        return s[start:start + minLen]