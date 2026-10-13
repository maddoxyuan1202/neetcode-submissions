class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ""
        for c in s:
            if c.isalnum():
                cleanS += c.lower()
        
        return cleanS == cleanS[::-1]

            