# 15. 3Sum

class Solution(object):
    nums = []

    def two_sum(self, left, target):
        # Use a list to store all cases where the two numbers sum up to target
        pairs = []

        # Note: `right` does not need to be passed in as argument
        # Because it will always start from the end of the array `nums`
        right = len(self.nums) - 1

        while left < right:
            pair_sum = self.nums[left] + self.nums[right]
            left_num = self.nums[left]
            right_num = self.nums[right]

            if pair_sum < target:
                # Keep moving `left` pointer until it's pointing to a different number
                # than current left_num to avoid duplicate pairs
                while left < right and self.nums[left] == left_num:
                    left += 1

            elif pair_sum > target:
                while left < right and self.nums[right] == right_num:
                    right -= 1

            else:
                pairs.append((left_num, right_num))

                while left < right and self.nums[left] == left_num:
                    left += 1
                while left < right and self.nums[right] == right_num:
                    right -= 1

        return pairs

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        # Sort the list so that we can use two pointers to solve two sum subproblem
        self.nums = nums
        self.nums.sort()

        for i in range(0, len(nums)):
            # Skip current element if it is same as previous value to avoid duplicates
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            # Find a pair of numbers that sum up to target from remaining numbers
            pairs = self.two_sum(i + 1, 0 - nums[i])

            # Add all possible triplets to results
            for pair in pairs:
                results.append((nums[i], pair[0], pair[1]))

        return results
