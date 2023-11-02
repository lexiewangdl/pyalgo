# 268. Missing Number
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # calculate sum of numbers from 0 to len(nums)
        expected_sum = 0
        for i in range(0, len(nums) + 1):
            expected_sum += i

        # calculate sum of numbers in array
        actual_sum = sum(nums)

        # find missing number
        return expected_sum - actual_sum

    def missingNumber(self, nums: List[int]) -> int:
        ans = 0  # space complexity: O(1)

        # sort nums, O(n log n)
        nums.sort(reverse=False)

        # for loop, O(n)
        for n in nums:
            if n == ans:
                ans += 1
            else:
                return ans

        return ans
