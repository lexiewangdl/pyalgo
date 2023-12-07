class Solution:
    result = []

    def backtrack(self, track, n, k) -> None:
        # terminating condition
        if len(track) == k:
            if sum(track) == n:
                self.result.append(track.copy())
            return

        # explore other options
        s = 1 if not track else track[-1] + 1  # only check numbers greater than last number in track
        # because to reach combination [4, 1, 2], another combination [1, 2, 4] must have already exist in list

        for i in range(s, 10):
            if i in track:
                continue

            # make selection
            track.append(i)

            # recursive call
            self.backtrack(track, n, k)

            # cancel selection
            track.pop()
        return

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []

        self.backtrack([], n, k)

        return self.result
