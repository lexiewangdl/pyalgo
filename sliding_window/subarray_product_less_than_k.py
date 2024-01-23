# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        l = 0
        r = 0

        window_prod = 1

        while r < len(nums):
            # update the product of numbers in window by value at index r
            window_prod *= nums[r]

            # shrink the window if:
            # (1) product of elements in window is greater than or equal to k
            # (2) left is smaller or equal to right (in case of index out of range error)
            while window_prod >= k and l <= r:
                window_prod /= nums[l]
                l += 1

            # (r - l) + 1
            result += r - l + 1
            r += 1

        return result

