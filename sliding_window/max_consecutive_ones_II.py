# 487.


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0

        left = 0
        right = 0

        flip_count = 0

        while right < len(nums):
            if nums[right] == 0:
                flip_count += 1

            while flip_count > 1:
                if nums[left] == 0:
                    flip_count -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result
