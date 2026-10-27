class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []


        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:

            # 从左往右
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # 从上往下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # 从右往左
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # 从下往上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res