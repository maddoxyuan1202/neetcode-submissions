class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        total = 0

        for i in range(n):
            total += digits[i] * pow(10, n-i-1)

        return [int(c) for c in str(total + 1)]