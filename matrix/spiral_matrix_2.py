# 59. Spiral Matrix II


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        result = [[0 for _ in range(n)] for _ in range(n)]

        # Define the boundaries
        upper, left = 0, 0
        lower, right = n - 1, n - 1

        i = 1
        while i < n * n + 1:
            # fill upper row
            if upper <= lower:
                for j in range(left, right + 1):
                    result[upper][j] = i
                    i += 1
                # update boundary
                upper += 1

            # fill right col
            if left <= right:
                for j in range(upper, lower + 1):
                    result[j][right] = i
                    i += 1
                right -= 1

            # fill lower row
            if upper <= lower:
                for j in range(right, left - 1, -1):
                    result[lower][j] = i
                    i += 1
                lower -= 1

            # fill left col
            if left <= right:
                for j in range(lower, upper - 1, -1):
                    result[j][left] = i
                    i += 1
                left += 1

        return result