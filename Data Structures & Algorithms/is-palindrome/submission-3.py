class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = []
        for ch in s:
            if ch.isalnum():
                cleanS.append(ch.lower())

        return cleanS == cleanS[::-1]
        