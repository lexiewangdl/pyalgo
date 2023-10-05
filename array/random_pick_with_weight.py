import random


class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0] * (len(w) + 1)
        self.w = w

        # initialize preSum array
        for i in range(len(w)):
            self.preSum[i + 1] = self.preSum[i] + w[i]

        # define range of random integer selection
        self.right_bound = self.preSum[len(self.preSum) - 1]

    def pickIndex(self) -> int:
        # generate a random number
        if len(self.w) == 1:
            return 0

        target = random.randint(1, self.right_bound)  # range is [1, preSum[n-1]] where n is length of preSum

        # find the index of target or the smallest element that's larger than target in preSum
        preSum_idx = self.binary_search_leftmost(target)

        # return index of corresponding item in w
        return preSum_idx - 1

    def binary_search_leftmost(self, target: int) -> int:
        left = 0
        right = len(self.preSum)

        while left < right:
            mid = left + (right - left) // 2
            if self.preSum[mid] == target:
                right = mid  # search to the left of found target
            elif self.preSum[mid] < target:
                left = mid + 1
            else:
                right = mid

        if right == len(self.preSum):
            return -1
        return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
