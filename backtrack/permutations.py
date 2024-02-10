class Solution:
    # Initialize list to store the result, which is a list of lists
    result = []

    def backtrack(self, path, choices, used):
        # end_condition: path is same length as choices, meaning that all choices have been used
        if len(path) == len(choices):
            # Create a copy to avoid changing the path
            self.result.append(path.copy())
            return

        # Check remaining choices
        for i in range(len(choices)):
            # If this item has been used
            if used[i]:
                continue

            # Make a choice
            used[i] = True  # Mark as used, so that it won't be used again
            path.append(choices[i])

            self.backtrack(path, choices, used)

            # Reverse choice
            path.pop()
            used[i] = False
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        used = [False] * len(nums)
        self.backtrack([], nums, used)
        return self.result
