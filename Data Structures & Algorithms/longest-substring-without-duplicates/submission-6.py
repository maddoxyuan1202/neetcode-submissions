class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        strSet = set()
        res = 0
        while r < len(s):
            if s[r] in strSet:
                strSet.remove(s[l])
                l += 1
            else:
                strSet.add(s[r])
                res = max(res, r - l + 1)
                r += 1

        return res