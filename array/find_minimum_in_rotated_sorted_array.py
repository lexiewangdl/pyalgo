# 153. Find Minimum in Rotated Sorted Array
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # When the left and right pointers meet, the minimum element is found
            if left == right:
                return nums[mid]

            elif nums[mid] > nums[right]:
                # Target number is toward right end of the search region
                left = mid + 1  # +1 because `mid` has been checked

            else:
                # Target number is toward left end of the search region
                right = mid  # Don't +1 because `mid` could be the target!

        return -1