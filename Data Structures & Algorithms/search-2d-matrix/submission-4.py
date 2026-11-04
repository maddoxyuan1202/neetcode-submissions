class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m-1

        while l <= r:
            mid = (l + r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                l1, r1 = 0, n - 1
                while l1 <= r1:
                    mid1 = (l1 + r1)//2
                    if target == matrix[mid][mid1]:
                        return True
                    elif target > matrix[mid][mid1]:
                        l1 = mid1 + 1
                    else:
                        r1 = mid1 - 1
                return False
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        return False

                
