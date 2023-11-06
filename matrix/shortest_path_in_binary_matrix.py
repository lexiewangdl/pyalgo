# 1091. Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
import collections
import math
from typing import List


class Solution:

    # shortest path:
    # start: 0, 0
    # end: m-1, n-1
    # all cells along the way must be 0

    # the resulting path length is number of cells visited

    # can move in all directions
    directions = [(1, 0), (0, 1), (1, 1),
                  (-1, 0), (0, -1), (-1, -1),
                  (1, -1), (-1, 1)] # down, right, down+right, (row_dir, col_dir, step_size)

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # definitely no clear path
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        elif grid[0][0] == 0 and m == 1 and n == 1:
            return 1

        q = collections.deque([(0, 0, 1)]) # (row, col, dist)

        # keep track of nodes visited
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True

        shortest_path_distance = math.inf

        while len(q) > 0:
            row, col, dist = q.popleft()

            # explore possible directions
            for d in self.directions:
                new_row = row + d[0]
                new_col = col + d[1]

                if new_row == m - 1 and new_col == n - 1:
                    shortest_path_distance = min(shortest_path_distance, dist + 1)

                # check if index is out of bound
                if not (new_row >= 0 and new_row < m and new_col >= 0 and new_col < n):
                    continue

                if visited[new_row][new_col]:
                    continue

                # check if this is a clear path
                if grid[new_row][new_col] == 1:
                    continue

                q.append((new_row, new_col, dist + 1))
                visited[new_row][new_col] = True

        return -1 if shortest_path_distance == math.inf else shortest_path_distance
