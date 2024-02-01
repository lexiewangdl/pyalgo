class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left: where the next processed element should be placed
        # right: the next element to be processed
        left, right = 0, 1
        count = 1

        while right < len(nums):
            # if left and right are pointing to the same element
            if nums[right] == nums[left]:
                if count < 2:
                    left += 1
                    nums[left] = nums[right]
                count += 1
            # if left and right are pointing to different elements
            else:
                left += 1
                nums[left] = nums[right]
                count = 1

            right += 1

        return left + 1