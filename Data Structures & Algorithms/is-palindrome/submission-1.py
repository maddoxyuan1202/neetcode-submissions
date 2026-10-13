class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [ch.lower() for ch in s if ch.isalnum()]

        l, s = 0, len(s_list)-1
        while l < s:
            if s_list[l] != s_list[s]:
                return False
            
            l +=1
            s -=1
        return True
            