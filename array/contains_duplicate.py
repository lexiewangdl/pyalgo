class Solution:

    # Time O(n log n), space O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the list
        nums.sort()

        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            else:
                prev = nums[i]

        return False

    # Time O(n), space O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for i in range(0, len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])

        return False
