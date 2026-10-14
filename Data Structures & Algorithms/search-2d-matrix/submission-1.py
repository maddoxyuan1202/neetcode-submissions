class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        have = 0
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1

            elif target > matrix[mid][-1]:
                l = mid + 1

            else:
                row = matrix[mid]
                break
        else:
            return False

        l, r = 0, len(row) - 1

        while l <= r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
