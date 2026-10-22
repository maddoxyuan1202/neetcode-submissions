class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        resIdx = 0
        resLen = 1

        dp = [[False] * n for _ in range(n+1)]
        for i in range(n):
            dp[i][i] = True

        if len(s) == 1:
            return s


        for length in range(2, n+1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = s[i] == s[j]
                    if dp[i][j]:
                        resIdx = i
                        resLen = length

                else:
                    if (s[i] == s[j] and dp[i+1][j-1]):
                        dp[i][j] = True
                        if dp[i][j] and length > resLen:
                            resIdx = i
                            resLen = length



        return s[resIdx: resIdx + resLen]