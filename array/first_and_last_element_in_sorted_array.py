# 34. Find First and Last Position of Element in Sorted Array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        # left boundary search
        l1 = 0
        r1 = len(nums)

        while l1 < r1:
            mid = l1 + (r1 - l1) // 2

            if nums[mid] == target:  # 找最左侧target，缩小右边界
                r1 = mid
            elif nums[mid] < target:  # search right
                l1 = mid + 1
            elif nums[mid] > target:
                r1 = mid

        # l1 = r1, result is l1

        # right boundary search
        l2 = 0
        r2 = len(nums)

        while l2 < r2:
            mid = l2 + (r2 - l2) // 2

            if nums[mid] == target:
                l2 = mid + 1
            elif nums[mid] < target:
                l2 = mid + 1
            elif nums[mid] > target:
                r2 = mid

        # result is l1-1

        result = [-1, -1]

        if l1 < len(nums):
            result[0] = l1 if nums[l1] == target else -1
        if l2 - 1 < len(nums):
            result[1] = l2 - 1 if nums[l2 - 1] == target else -1

        return result