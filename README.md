# The Ultimate LeetCode Cheatsheet
This repository contains solutions to LeetCode problems written in Python3, stored
in different folders based on their topics. 

💡 The current file is a cheatsheet that contains the most important algorithms and
data structures and what kind of problems they are useful for. 


## Topics
1. [Two pointers](#1-two-pointers) / 双指针
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
7. [Graph algorithms](#7-graph-algorithms) / 图
8. [String](#8-string-problems)
   1. [Palindrome problems](#81-palindrome-problems--回文串问题) / 回文串
9. [Interesting problems](#9-interesting-problems)
   1. [Selling and buying stocks](#91-selling-and-buying-stocks) / 股票买卖
   2. [Trapping rain water](#92-trapping-rain-water) / 接水
   3. [Palindrome problems](#93-palindrome-problems) / 回文串
      1. [Palindrome problems on strings](#931-palindrome-problems-on-strings) / 字符串回文串
      2. [Palindrome problems on linked lists](#932-palindrome-problems-on-linked-lists) / 链表回文串
      3. [Palindrome problems on arrays](#933-palindrome-problems-on-arrays) / 数组回文串
      4. [Palindrome problems on integers](#934-palindrome-problems-on-integers) / 整数回文串

## 1. Two Pointers

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

## 7. Graph Algorithms

### 7.1. Topological Sort

### 7.2

### 7.3. Union Find

### 7.4

### 7.5

## 8. String Problems

### 8.1 Palindrome Problems / 回文串问题
1. 判断回文串：对撞指针，从两端收缩，判断回文串 (Example: [125. Valid Palindrome](string/valid_palindrome.py))
2. 寻找回文串：中心扩散法，从中间向两端扩散，寻找回文串 (Example: [5. Longest Palindromic Substring](two_pointers/longest_palindromic_substring.py))

More on palindrome problems: [Palindrome Problems](#93-palindrome-problems)

## 9. Interesting Problems

### 9.1. Selling and buying stocks

### 9.2. Trapping rain water
思路：不要去思考整体能装多少水，而是每个位置`i`能装多少水。每个位置`i`能装多少水取决于`i`左边最高的柱子和`i`右边最高的柱子中较矮的那个。

方法：用**对撞指针**，从两端收缩，每次收缩较矮的那个柱子，同时更新结果。Use [two pointers](#1-two-pointers) that move in the opposite direction (moving towards the middle), and each time move the pointer that is pointing to the _shorter bar_. Update the result at each step.

[Python solution](two_pointers/trapping_rain_water.py)

### 9.3. Palindrome problems
Palindrome problems can be divided into multiple categories based on the _data structure_ used to store the palindrome:
1. String
2. Linked list
3. Array
4. Integer

#### 9.3.1. Palindrome problems on strings
Palindrome problems on strings are usually solved using [two pointers](#1-two-pointers).

1. 判断回文串 Check palindrome:
   - 用**对撞指针**，从两端收缩，判断回文串
   - Example: [125. Valid Palindrome](string/valid_palindrome.py)
2. 寻找回文串 Find palindrome
   - 用**中心扩散法**，从中间向两端扩散，寻找回文串
   - Example: [5. Longest Palindromic Substring](two_pointers/longest_palindromic_substring.py)

#### 9.3.2. Palindrome Problems on Linked Lists

先找链表中点，再反转后半段链表。

Because you can only move in _a single direction_ in a linked list, we can't use two pointers and make then move in 
opposite directions. However, we can find the _mid-point_ of a linked list, and then _reverse_ the latter
half of the linked list.

```shell
# Input
1 -> 2 -> 3 -> 2 -> 1
# After processing
1 -> 2 -> 3 <- 2 <- 1
```

Example: [234. Palindrome Linked List](linked_lists/palindrome_linked_list.py)

#### 9.3.3 Palindrome Problems on Arrays

Basically the same as palindrome problems on strings.

#### 9.3.4 Palindrome Problems on Integers
Do not convert the integer to a string and then check if the string is a palindrome! Very inefficient.

The intuition is to _reverse the integer_ and simply use `==` to check if reversed integer is equal to the original integer.
Use two variables: `y` is the reversed integer, and `temp` is an integer we use to find each digit of input `x`.
Initialize `temp = x`, while `temp > 0`, find the last digit using `digit = temp % 10`, and then update `temp` using integer division `temp = temp // 10`.
Update `y` at each step, `y = y * 10 + digit`. Finally, check if `y == x`.



Example: [9. Palindrome Number](math/palindrome_number.py)


