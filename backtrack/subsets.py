# 78. Subsets

class Solution:
    result = []

    def backtrack(self, path, choices, start):
        # every node in the tree is a valid subset
        # so we add the path to the result at every node
        self.result.append(path.copy())

        for i in range(start, len(choices)):
            # make a selection
            path.append(choices[i])

            # the next 'start' should be i+1 because the i-th element is already selected
            # and the elements that precede the i-th element will be covered by subtrees to the left
            # avoid selecting the same element twice
            self.backtrack(path, choices, i + 1)

            # undo the selection
            path.pop()

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack([], nums, 0)
        return self.result