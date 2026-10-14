class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""

        countS = {}
        countT = {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        need = len(countT)
        have = 0

        l = 0
        minLen = float("inf")
        result = ""

        for r in range(len(s)):
            ch = s[r]
            countS[ch] = countS.get(ch, 0) + 1

            # 当前字符的数量刚好达到要求
            if ch in countT and countS[ch] == countT[ch]:
                have += 1

            # 当前窗口已经包含 t 所需的全部字符
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    result = s[l:r + 1]

                leftChar = s[l]
                countS[leftChar] -= 1

                # 移除后，该字符不再满足要求
                if leftChar in countT and countS[leftChar] < countT[leftChar]:
                    have -= 1

                l += 1

        return result