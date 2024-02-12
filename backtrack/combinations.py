# 77. Combinations

class Solution:
    result = []
    k = 0
    n = 0

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.k = k
        self.n = n
        self.backtrack([], 1)
        return self.result

    def backtrack(self, path, start):
        # end condition:
        if len(path) == self.k:
            self.result.append(path.copy())
            return

        for i in range(start, self.n + 1):
            # make a selection
            path.append(i)

            self.backtrack(path, i + 1)

            # undo selection
            path.pop()

        return
