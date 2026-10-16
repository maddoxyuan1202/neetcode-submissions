class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s, key = lambda x:x, reverse = True) == sorted(t, key = lambda x:x, reverse = True)
        