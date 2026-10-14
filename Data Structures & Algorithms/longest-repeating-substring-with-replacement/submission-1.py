class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        listS = list(s)
        l, r, size = 0, 0, len(listS)
        strSet = {}
        maxLength = 0
        win_length = 0
        max_count = 0
        while r < size:
            strSet[listS[r]] = strSet.get(listS[r], 0) + 1
            r += 1

            max_count = max(strSet.values())

            while (r - l) - max_count > k:
                strSet[listS[l]] -= 1
                l += 1
                max_count = max(strSet.values())

            win_length = r - l
            maxLength = max(maxLength, win_length)

        return maxLength