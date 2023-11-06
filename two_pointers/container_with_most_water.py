# 11. Container with most water
# https://leetcode.com/problems/container-with-most-water/description/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        l_max = 0
        r_max = 0

        max_amount = 0

        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            # update pointer, one at a time
            if l_max < r_max:
                max_amount = max(max_amount, l_max * (right - left))
                left += 1
            else:
                max_amount = max(max_amount, r_max * (right - left))
                right -= 1

        return max_amount
