# 18. FOUR SUM
class Solution(object):
    def two_sum(self, nums, start, target):
        left = start
        right = len(nums) - 1

        pairs = []

        while left < right:
            pair_sum = nums[left] + nums[right]
            left_val = nums[left]
            right_val = nums[right]

            if pair_sum < target:
                while left < right and nums[left] == left_val:
                    left += 1
            elif pair_sum > target:
                while left < right and nums[right] == right_val:
                    right -= 1
            else:
                pairs.append([left_val, right_val])
                while left < right and nums[left] == left_val:
                    left += 1
                while left < right and nums[right] == right_val:
                    right -= 1

        return pairs

    def three_sum(self, nums, start, target):
        triplets = []

        for i in range(start, len(nums)):
            # Avoid duplicates by checking if current number is same as previous number
            if i > start and nums[i] == nums[i-1]:
                continue

            pairs = self.two_sum(nums, i+1, target - nums[i])

            # Add pairs to results
            for p in pairs:
                triplets.append([nums[i], p[0], p[1]])

        return triplets

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        # Sort input array
        nums.sort()

        for i in range(0, len(nums)):
            # Avoid duplicates by checking if current number is same as previous number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            triplets = self.three_sum(nums, i+1, target - nums[i])

            # Add triplets to results
            for t in triplets:
                results.append([nums[i], t[0], t[1], t[2]])

        return results