# 90. Subsets II

class Solution:
    result = []
    nums = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        # sort the numbers so that items with same value are next to each other
        self.nums = sorted(nums)

        self.backtrack([], 0)

        return self.result

    def backtrack(self, path, start):
        # add path to result
        self.result.append(path.copy())

        for i in range(start, len(self.nums)):
            # avoid duplicate subsets
            # if neighboring branches have the same value, prune current branch
            if i > start and self.nums[i] == self.nums[i - 1]:
                continue

            # make a selection
            path.append(self.nums[i])

            self.backtrack(path, i + 1)

            # undo selection
            path.pop()

        return
