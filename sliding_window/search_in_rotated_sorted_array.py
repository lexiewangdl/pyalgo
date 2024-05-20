# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] < nums[mid]: # Left part correct order
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            else: # Right part correct order
                if target > nums[mid] and target <= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid

        return left if left < right and nums[left] == target else -1
