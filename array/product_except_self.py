# 238. Product of Array Except Self
class Solution(object):

    # O(1) extra space
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        # Calculate the product of all elements to the left of i-th element
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]

        # Calculate the product of all elements excluding i-th element
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product = right_product * nums[i]

        return answer

    # O(3n) time, O(2n) extra space
    def productExceptSelf_Slow(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [-1] * len(nums)

        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]

        for i in range(0, len(nums)):
            answer[i] = left_product[i] * right_product[i]

        return answer