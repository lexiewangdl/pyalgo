# The Ultimate LeetCode Cheatsheet
This repository contains solutions to LeetCode problems written in Python3, stored
in different folders based on their topics. 

💡 The current file is a cheatsheet that contains the most important algorithms and
data structures and what kind of problems they are useful for. 


## Topics
1. [Two pointers](#two-pointers) (linked list and array)
2. [Binary trees](#binary-trees)
3. Arrays
   1. Prefix sum algorithm
   2. [Sliding window](#sliding-window)
   3. [Binary search](#binary-search-on-arrays)
      1. [Find left-most target](#look-for-left-most-target)
      2. [Find right-most target](#look-for-right-most-target)
4. Linked lists
5. Dynamic programming
6. Math
7. Graph algorithms
8. [Interesting problems](#interesting-problems)
   1. [Selling and buying stocks](#1-selling-and-buying-stocks)
   2. [Trapping rain water](#2-trapping-rain-water)

## Two Pointers

1. **快慢指针** Slow and fast pointers, in the same direction
   - Linked Lists
      - 找链表中点 Find the middle point of a linked list （慢指针走一步，快指针走两步）
      - 找链表第n个节点 Find the n-th node from the end of a linked list  (快指针先走n步，然后快慢指针同时前进)
      - 判断链表是否有环 Check if a linked list has a cycle（慢指针走一步，快指针走两步）
   - Array
     - Remove redundant elements in a sorted array （慢指针左侧是已经处理好的元素，快指针指向现在要处理的元素）
     - [Move zeroes](two_pointers/move_zeroes.py) （慢指针左侧是已经处理好的元素，快指针指向现在要处理的元素）
   - String
     - [String compression](two_pointers/string_compression.py) (e.g. "aabbccc" -> "a2b2c3")
   - 滑动窗口 More complicated scenario: [Sliding Window](#sliding-window)
     - 什么时候扩大窗口？什么时候缩小窗口？什么时候更新结果？
2. **对撞指针** Pointers that move in the opposite direction
   - [Binary Search](#binary-search-on-arrays)
   - 有序数组两数之和 [Two sum in a sorted array](two_pointers/two_sum_2.py)
   - 判断回文串 Check palindrome 
   - [Trapping rain water](two_pointers/trapping_rain_water.py)
3. **分离指针** Pointers on different arrays
   - Merge two sorted arrays
   - Merge sort
   - 找两个数组的交集：sort后用分离双指针

## Binary Trees

Key questions:



## Arrays
### Sliding Window
Key Questions:
1. 什么时候扩大窗口？
2. 什么时候缩小窗口？
3. 什么时候更新结果？


Template:
```python
def sliding_window(s: str, t: str):
    left = 0
    right = 0
    
    window = dict()  # what we have currently in our window
    need = dict()  # the chars we need (keys) and each char's corresponding count (values)
    
    valid = 0  # total number of valid keys 
               # a valid key's count in window must be greater or same as in need
    
    # store chars in t in dictionary need
    for c in t:
        need[c] = need.get(c, 0) + 1
    
    while right < len(s):
        c = s[right]
        right += 1  # increment immediately after getting c
        
        # update window data
        ...
        
        # check whether window needs shrink
        while left < right and window_needs_shrink:
            d = s[left]
            left += 1
            
            # update window data
            ...
```

Key points:
1. Initialize `left` and `right` to be zero, immediately increment `left` and `right` right after getting the corresponding character
2. **Time complexity is O(N)** because even through there is an embedded `while` loop, the pointers `left` and `right` will only increase, and never decrease. Every single element in array (or string) will only be added to the `window` once, and removed from it once (at max).
3. `...` means we need to update data stored in `window`. The first instance is when we add new element, the second is when we remove an element.


### Binary Search on Arrays
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

#### Look for left-most target
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

#### Look for right-most target
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

## Linked Lists

### 1. 反转链表 Reverse a linked list

## Interesting Problems

### 1. Selling and buying stocks

### 2. Trapping rain water
重点：不要去思考整体能装多少水，而是每个位置`i`能装多少水。每个位置`i`能装多少水取决于`i`左边最高的柱子和`i`右边最高的柱子中较矮的那个。

[Python solution](two_pointers/trapping_rain_water.py)


