# 704. Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (right - left) // 2 + left

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # search left
                right = mid
            elif nums[mid] < target:
                # search right
                left = mid + 1

        return -1
