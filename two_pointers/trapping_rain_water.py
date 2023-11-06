#  42. Trapping Rain Water
# Problem Description: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        l_max = 0
        r_max = 0

        res = 0

        while left < right:
            # update max bar height seen
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            # update result
            if l_max < r_max:  # the max height of bar we've seen on left is smaller
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1

        return res