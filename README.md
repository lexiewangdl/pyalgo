# pyalgo
This repository contains solutions to LeetCode problems written in Python3.

## Topics
1. Two pointers (linked list and array)
2. Binary tree
3. Dynamic programming
4. Linked lists
5. Arrays
6. Math

## Binary Search (Arrays)
Code structure:
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

### Look for left-most target
```python
def search_left_bound(nums: list, target: int):
    left = 0
    right = len(nums)  # ** important **
    
    while left < right:  # ** important **
        mid = left + (right - left) // 2  # use // operator and avoid overflow
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid  # right is exclusive
        elif nums[mid] < target:
            left = mid + 1  # left is inclusive

    # make sure that index `right` is not out of bounds
    if right == len(nums) or nums[right] != target:
        return -1
    else:
        return right  # or return left because they are equal
```

How to check whether `target` was found or not?
- If `target` was found, `left` will be the index of the target
- If `target` was not found, `left` will be the index of the first element that is greater than `target`
- Prior to returning, check if the element at `left` is equal to `target`:
  - `return nums[left] == target ? left : -1`

Why return `left` and not `right`?
- It's the same thing
- When we exit while loop, `left` and `right` will be equal

Why this method can find the left-most target?
- When `nums[mid] == target`, we update `right = mid`
- This will cause the search to continue on the left side of `mid`
- This means that once we have found a target, we will keep looking for more targets on the left side of `mid`

### Look for right-most target
```python
def search_right_bound(nums: list, target: int):
    left = 0
    right = len(nums)  # ** important **
    
    while left < right:  # ** important **
        mid = left + (right - left) // 2 
        if nums[mid] == target:
            left = mid + 1  # ** important **
        elif nums[mid] < target:
            left = mid + 1 
        elif nums[mid] < target:
            right = mid
            
    # make sure that index `left - 1` is not out of bounds
    if left == 0 or nums[left - 1] != target:
        return -1
    else:
        return left - 1  # ** important **
```

Why this method can find the right-most target?
- Whenever we have found a target, we update `left = mid + 1`
- This will cause the search to continue on the right side of `mid`
- This means that once we have found a target, we will keep looking for more targets on the right side of `mid`
- If there are no more targets on the right side of `mid`, `left` will be the index of the first element that is greater than `target`
- Prior to returning, we return `left - 1` to get the index of the right-most target

Why return `left - 1` and not `right`?
- When exiting the while loop, `left` and `right` will be equal
- However, since the way we update `left` is `left = mid + 1`,
when we exit the while loop, `nums[left]` is not necessarily equal to `target`

What if `nums` doesn't contain `target`?
- Prior to returning, check if the element at `left - 1` is equal to `target`:
  - `return nums[left - 1] == target ? left - 1 : -1`

Why check whether `left - 1` is out of bounds?
- The range of `left` is `[0, len(nums)]`, because when we exit the while loop, 
`left` and `right` will be equal
- If `left == 0`, then `left - 1` will be out of bounds, this happens when the left pointer has never moved
