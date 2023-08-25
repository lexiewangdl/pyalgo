# Two Pointers


## Two Pointers on Arrays

Date: Aug 24
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

### 83. Remove Duplicates from Sorted List (Easy)
**My solution**:

Similar to previous problem, use two pointers. 
`p1` represents the last unique element (note that this is a little different from last question,
where `j-1` is the last unique element and `j` is the index where next unique element should be placed at).
This is because once we found the next unique element, we would want to make `p1.next` point to the next unique element.
`p2` is the next element to be checked. If `p2.val == p1.val`, it suggests that `p2` is a duplicate
of `p1`, so we only move `p2` pointer to its next node, which is same as ignoring this node. If `p2.val != p1.val`,
we have found the next unique element in linked list, at this point, we make `p1.next` point to `p2`, which is
same as deleting all nodes in between.

At the end, it's important to set `p1.next = None`, this is because there could be trailing duplicates at the end. For example, 
if linked list is `1 -> 2 -> 3 (p1) -> 3 -> None (p2)`, since `p2` is already out of linked list, we are out of
the while loop, but `p1.next` is still pointing to a trailing duplicate node.
Since we know for sure that `p1` is the last unique node, we can safely delete all trailing nodes.