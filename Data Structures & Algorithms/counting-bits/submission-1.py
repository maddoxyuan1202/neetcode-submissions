class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            num = i

            while num > 0:
                if num & 1:
                    res[i] += 1
                num >>= 1

        return res