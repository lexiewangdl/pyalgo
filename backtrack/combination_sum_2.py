# 40. Combination Sum II

class Solution:
    result = []
    candidates = []
    path = []
    target = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.target = target

        # sort the array to avoid adding duplicates to result
        self.candidates = sorted(candidates)
        self.path = []

        self.backtrack(0, 0)

        return self.result

    def backtrack(self, path_sum, start):
        # save result if sum of elements is equal to target
        if path_sum == self.target:
            self.result.append(self.path.copy())
            return

        # if path_sum gets bigger than target, stop expanding the subtree
        if path_sum > self.target:
            return

        for i in range(start, len(self.candidates)):
            # avoid duplicates in results
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue

            # all possible numbers are positive integers,
            # if the number itself is greater than target, no need to consider
            if self.candidates[i] > self.target:
                continue

            # make a selection
            self.path.append(self.candidates[i])
            path_sum += self.candidates[i]

            self.backtrack(path_sum, i + 1)

            # undo selection
            self.path.pop()
            path_sum -= self.candidates[i]

        return
