"""
27. Remove Element
"""


def remove_element(nums: list, val: int) -> int:
    j = 0  # Number of elements that is NOT equal to val, also index where next un-equal element should be placed
    for i in range(len(nums)):
        if nums[i] != val:  # Found element that's not equal to val
            nums[j] = nums[i]  # Set value at j to be value at i
            j += 1

    return j
