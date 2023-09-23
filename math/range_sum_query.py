# 303. Range Sum Query
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.memo = [0] * (len(nums) + 1)
        self.nums = nums
        self.fillMemo()

    def fillMemo(self):
        for i in range(1, len(self.memo)):
            self.memo[i] = self.memo[i-1] + self.nums[i-1]
        return

    def sumRange(self, left: int, right: int) -> int:
        return self.memo[right+1] - self.memo[left]

