# 304. Range Sum Query 2D - Immutable
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.memo = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        self.matrix = matrix
        self.initializeMemo()

    # initializeMemo() works on O(n^2) time complexity
    def initializeMemo(self):
        for i in range(1, len(self.matrix) + 1):
            for j in range(1, len(self.matrix[0]) + 1):
                self.memo[i][j] = self.memo[i - 1][j] + self.memo[i][j - 1] - self.memo[i - 1][j - 1] + \
                                  self.matrix[i - 1][j - 1]
        return

    # sumRegion() works on O(1) time complexity
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.memo[row2 + 1][col2 + 1] - self.memo[row2 + 1][col1] - self.memo[row1][col2 + 1] + self.memo[row1][
            col1]
        # all_sum = self.memo[row2+1][col2+1]
        # bottom_left = self.memo[row2+1][col1]
        # top_right = self.memo[row1][col2+1]
        # top_left = self.memo[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
