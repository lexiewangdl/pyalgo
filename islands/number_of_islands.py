# 200. Number of Islands
class Solution:
    m = 0
    n = 0

    def dfs(self, i, j, grid):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return

        # If in water, stop checking
        if grid[i][j] == "0":
            return

        # If on island, make it water
        grid[i][j] = "0"

        self.dfs(i + 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i - 1, j, grid)
        self.dfs(i, j - 1, grid)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    # Discovered a new island
                    num_islands += 1

                    # Make this island disappear
                    self.dfs(i, j, grid)

        return num_islands
