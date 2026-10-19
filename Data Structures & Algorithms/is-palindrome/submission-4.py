class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_copy = []
        for ch in s:
            if ch.isalnum():
                s_copy.append(ch.lower())
        return s_copy == s_copy[:: -1]