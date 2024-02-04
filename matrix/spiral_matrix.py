# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Define the border
        top = 0
        down = num_rows - 1
        left = 0
        right = num_cols - 1

        # Define the resulting list
        result = []

        # while the entire matrix has not been fully traversed
        while len(result) < num_rows * num_cols:
            # move from top left to top right
            if top <= down:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                # move upper bound
                top += 1

            # move from top right to bottom right
            if left <= right:
                for i in range(top, down + 1):
                    result.append(matrix[i][right])
                # move right bound
                right -= 1

            # move from bottom right to bottom left
            if top <= down:
                for i in range(right, left - 1, -1):
                    result.append(matrix[down][i])
                # move lower bound
                down -= 1

            # move from bottom left to top left
            if left <= right:
                for i in range(down, top - 1, -1):
                    result.append(matrix[i][left])
                # move left bound
                left += 1

        return result