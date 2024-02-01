# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return None

        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            # Compare the two elements
            if nums1[p1] >= nums2[p2]:
                nums1[p1 + p2 + 1] = nums1[p1]
                p1 -= 1
            else:
                nums1[p1 + p2 + 1] = nums2[p2]
                p2 -= 1

        # Check if reached the beginning of both arrays

        while p2 >= 0:
            nums1[p1 + p2 + 1] = nums2[p2]
            p2 -= 1

        return