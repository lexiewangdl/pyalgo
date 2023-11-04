# 380. Single Element in a Sorted Array


class Solution:
    # # maths
    def singleNonDuplicate(self, nums) -> int:
        return sum(set(nums)) * 2 - sum(nums)

    # Binary search
    def singleNonDuplicate(self, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # if the index of middle element is odd, subtract 1 to make it even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2

        return nums[left]

    # Naive solution
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] != num:
                # check if count is 2
                if count < 2:
                    return num
                else:
                    num = nums[i]
                    count = 1
            else:
                count += 1

        # last element
        return num