class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        count1 = {}
        count2 = {}
        if m > n:
            return False
        
        for i in range(m):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        if count1 == count2:
            return True

        for i in range(m, n):
            count2[s2[i]] = count2.get(s2[i], 0) + 1
            count2[s2[i-m]] -= 1
            if count2[s2[i-m]] == 0:
                del count2[s2[i-m]]
            if count1 == count2:
                return True

        return False
