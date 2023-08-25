"""
Date: Aug 24, 2023

26. Remove Duplicates from Sorted Array (Easy)

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements
in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present
in nums initially. The remaining elements of nums are not important as well as the size of nums.

Return k.
"""


# Better solution
def removeDuplicates(nums: list) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j


# My solution
def remove_duplicates(nums: list) -> int:
    if len(nums) == 1:
        return 1

    p1, p2 = 0, 1

    while p2 < len(nums):
        if p1 > 0 and nums[p1] <= nums[p1 - 1]:
            nums[p1] = nums[p2]
        while p2 < len(nums) and nums[p1] == nums[p2]:
            p2 += 1
        p1 += 1

    return p1


print(remove_duplicates([1, 2]), "\n")
print(remove_duplicates([1, 1]), "\n")
print(remove_duplicates([1, 2, 2]), "\n")

print(remove_duplicates([1, 1, 2, 2, 3]), "\n")
print(remove_duplicates([1, 2, 3, 4, 5]), "\n")
print(remove_duplicates([1, 1, 1, 4, 6]), "\n")

print(remove_duplicates([1]), "\n")
