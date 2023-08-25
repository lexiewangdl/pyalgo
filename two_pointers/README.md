# Two Pointers


## Two Pointers on Arrays
### 26. Remove Duplicates from Sorted Array (Easy)
**My solution**: to remove duplicates from sorted array in place, use two pointers to keep track of elements.
All elements to the left of the L pointer are elements we have checked and processed, and the element pointed to by the R pointer
is the next unique element that we haven't checked and processed.

If the length of input array is 1, the array is guaranteed to only have 1 unique element. No need to change input array.

While R pointer hasn't reached end of array, swap L element with R if L element is equal to or less than element at L-1.
(input array is sorted, if L element is less than L-1, it suggests that the element at L-1 has been swapped with a unique element).

Time complexity: O(N)

Space complexity: O(1)

**Better solution**:

`i` is the pointer we use to loop through the array (i.e. check every element in array).
`j` represents how many elements is unique. Since we are going to put all unique elements in the first `j` indices to the left
of the array, elements at indices `0` through `j-1` inclusive have all been confirmed to be unique, thus, `j` can also be thought of as the index where next unique element should be placed at.

The starting value of `j` is 1 because the first element is definitely unique.
`i` starts at 1 because we start by checking the second element in array. 
If `nums[i] != nums[i-1]`, we have found another unique element, and this element should be placed at index `j`. After updating the value at `j`, increment `j` by one.

In this case, `j` is very similar to `size` of a list data structure (which is different from `length` of a list data structure).

```python3
def removeDuplicates(nums: list) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
```