# Array Problems

## Table of Contents
- 704 - Binary Search 🍏
- 34 - Find First and Last Position of Element in Sorted Array 🍊

### 704. [Binary Search](https://leetcode.com/problems/binary-search/description/) (Easy)
Binary search (of array) code structure:
```python
def search(nums: list, target: int):
    left = 0
    right = len(nums)  # right = len(nums-1)
    
    while left < right:  # while left <= right, if inclusive
        mid = left + (right - left) // 2  # use // operator and avoid overflow
        if nums[mid] == target:
            ...
        elif nums[mid] < target:
            left = ...  # update left pointer
        else:
            right = ... # update right pointer
    
```

- Starting index of `right` can be either `len(nums)` or `len(nums-1)`, depending on whether the right index is inclusive or not
- `while left < right` or `while left <= right` depends on whether the right index is inclusive or not
- Calculating the mid point: `mid = left + (right - left) // 2` is the most accurate way to avoid overflow
  - Using `mid = (left + right) // 2` is not accurate because `left + right` may overflow
  - Using `//` operator is more efficient than using `/` operator because `/` gives a float number
- Updating the left and right pointers:
  - If `right` is inclusive, it can be updated as `right = mid - 1`, to avoid including mid in the next search
  - If `right` is exclusive, it can be updated as `right = mid`


### 34. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/) (Medium)
See [this page](README.md) for binary search template.

Basically, do binary search once to find the left-most target, and search again to find 
the right-most target.

