# 209. Minimum Size Subarray Sum
import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = math.inf

        left = 0
        right = 0

        window_sum = 0

        while right < len(nums):
            # add the value at index right to window_sum
            window_sum += nums[right]

            # compare window_sum to target
            while window_sum >= target:
                # update min_len
                min_len = min(min_len, right - left + 1)
                # update the window
                window_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != math.inf else 0
