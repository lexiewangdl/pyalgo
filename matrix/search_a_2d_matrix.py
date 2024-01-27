# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_u, row_d = 0, len(matrix)

        # Identify the row in which the target should be in
        while row_u < row_d:
            row_mid = row_u + (row_d - row_u) // 2

            # check if target is in current row
            if target == matrix[row_mid][0] or target == matrix[row_mid][-1]:
                return True

            elif matrix[row_mid][0] < target < matrix[row_mid][-1]:
                row_u = row_mid
                break

            if target < matrix[row_mid][0]:
                row_d = row_mid

            elif target > matrix[row_mid][-1]:
                row_u = row_mid + 1

        if row_u == len(matrix):
            return False

        # search the middle row
        left, right = 0, len(matrix[0])

        while left < right:
            mid = left + (right - left) // 2

            if matrix[row_u][mid] == target:
                return True

            elif target < matrix[row_u][mid]:
                right = mid

            else:
                left = mid + 1

        return False