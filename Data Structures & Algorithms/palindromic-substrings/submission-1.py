class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n+1)]
        res = 0

        for length in range(1, n+1):
            for i in range(0, n - length + 1):
                j = i + length -1
                if (dp[i+1][j-1] or (j - i <= 2 )) and s[i]==s[j]:
                    res += 1
                    dp[i][j] = True

        return res