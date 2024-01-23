# The Ultimate LeetCode Cheatsheet

This repository contains solutions to LeetCode problems written in Python3, stored
in different folders based on their topics.

💡 The current file is a cheatsheet that contains the most important algorithms and
data structures and what kind of problems they are useful for.

## Topics

1. [Two pointers](#1-two-pointers) / 双指针
2. [Binary trees](#2-binary-trees) / 二叉树
   1. [Traversal](#21-traversal) / 遍历
   2. [Divide and conquer](#22-divide-and-conquer) / 分治
   3. [Depth-first search (DFS)](#23-depth-first-search-dfs) / 深度优先搜索
   4. [Breadth-first search (BFS)](#24-breadth-first-search-bfs) / 广度优先搜索
   5. [DFS vs. BFS](#25-dfs-vs-bfs) / 深度优先搜索 vs. 广度优先搜索
3. [Arrays](#3-arrays) / 数组
   1. [Prefix sum algorithm](#31-prefix-sum-algorithm) / 前缀和数组
   2. [Difference array](#32-difference-array) / 差分数组
   3. [Sliding window](#33-sliding-window) / 滑动窗口
   4. [Binary search](#34-binary-search-on-arrays) / 二分查找
      1. [Find left-most target](#look-for-left-most-target) / 查找左边界
      2. [Find right-most target](#look-for-right-most-target)  / 查找右边界
   5. Heap
   6. Stack
   7. Queue
4. Linked lists
5. Recursion
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

## 2. Binary Trees

Whenever you see a binary tree question, ask yourself the following questions:

1. 能否**遍历**二叉树得到结果？ / Can I solve this problem by _**traversing**_ the tree once?
2. 能否用**分治**的思想，用子问题（子树）的解来得到原问题（树）的解？ / Can I use _**divide and conquer**_, and use the solution of the sub-problem (subtree) to find the answer to the original problem (tree)?
3. 在每个**节点**，我应该做什么？我应该在什么时候（前中后序）做？/ What should I do at each _**node**_? When should I do it (i.e. pre-order, in-order, post-order)?

All binary tree problems can be solved using either **traversal** or **divide and conquer**.

### 2.1. Traversal

The return type of traversal helper method is usually `None`.
No value is returned.
Instead, this method updates a _global variable_ to store the result.
The key is to choose the correct [order of traversal](#23-depth-first-search-dfs).

```python
result = None  # global variable

def traverse(root):
    if not root:
        return
  
    # Pre-order traversal
    ...
  
    traverse(root.left)
  
    # In-order traversal
    ...
  
    traverse(root.right)

    # Post-order traversal
    ...
```

### 2.2. Divide and Conquer

The return type of divide and conquer helper method is usually the same type as the _output_,
but it depends on the problem.

### 2.3. Depth-first Search (DFS)

1. Pre-order traversal / 前序遍历 = 根左右
   - 通常如果题目对遍历位置不敏感，就用前序遍历，没什么特别的。
   - 一棵二叉树的前序遍历结果 = 根节点 + 左子树的前序遍历结果 + 右子树的前序遍历结果
   - Time complexity O(N), space complexity O(h) where _h_ is height of tree. If we don't consider call stack, then space complexity is O(1).
   - e.g. Quick sort
2. In-order traversal / 中序遍历 = 左根右
   - 主要用于Binary search tree (BST)
   - BST 的中序遍历结果为 _non-decreasing_ order
   - Time complexity O(N), space complexity O(h) where _h_ is height of tree. If we don't consider call stack, then space complexity is O(1).
   - e.g. Binary search tree
3. Post-order traversal / 后序遍历 = 左右根
   - 后续遍历十分特殊，因为 post-order operations have access to information passed up from the children (sub-trees).
   - 一旦题目和**子树**有关，大概率要给函数设置一个返回值，然后用后续遍历。
   - Use cases: e.g. merge sort, _delete_ a node from a binary tree, subtree problems

**Summary**:

- 前序位置的代码执行是**自顶向下**的，后续位置的代码执行是**自底向上**的。
- 前序位置的代码只能access从parent node传递下来的数据，而后续位置的代码可以利用children nodes传递上来的数据。
- 前序位置的代码在刚刚**进入**某个节点时执行，中序位置的代码在左子树遍历完成，即将开始遍历右子树的时候执行，后续位置的代码在将要**离开**某个节点时执行。

### 2.4. Breadth-first Search (BFS)

1. Use FIFO queue
   - In Python, use `collections.deque` to implement queue, more efficient than `queue.Queue`
2. Add root node to queue first
3. While queue is not empty, pop first node, add its children to queue

### 2.5. DFS vs. BFS

When to use DFS? When to use BFS?

- BFS uses O(w) extra memory, where w is the maximum width of the tree
  - Maximum width of a binary tree is 2^(h), where _h_ is the height of the tree and _h_ starts from 0
  - Worst case: a binary tree is a linked list, then _h_ is equal to _N_
  - Height of a _balanced_ tree is O(log N)
- DFS uses extra space because of the _functional call stack_, O(h) extra space.
- 如果 tree 是 balanced，那么BFS需要的extra space更多；如果 tree 是 linked list，那么DFS需要的extra space更多。
- DFS 通常都是 recursive code, use call stack, BFS 通常都是 iterative code, use queue.
- BFS starts visiting from _root_, DFS starts visiting from _leaves_. 如果你要找的target更接近于root，那么BFS更适合。

### 2.6. Binary Tree Questions

#### 2.6.1. Construct Binary Trees

**构造二叉树**问题一般都用divide and conquer, 构造一棵树 = 构造根节点 + 构造左子树 + 构造右子树。

#### 2.6.2 Serialize and Deserialize Binary Trees

**序列化和反序列化**二叉树，需要利用对不同遍历顺序的理解，总结为：

当二叉树中的节点没有重复时：

1. 如果序列化结果**不包含空指针信息** / If serialization result **does not contain null pointers** ...
   - 只用一种遍历顺序是无法还原二叉树的，需要两种遍历顺序！
   - 如果用两种遍历顺序，以下组合可以还原二叉树：
     - 前序遍历 + 中序遍历 / Pre-order + In-order
     - 中序遍历 + 后序遍历 / In-order + Post-order
   - 如果用前序+后序，是无法还原二叉树的。
2. 如果序列化结果**包含空指针信息** / If serialization result **contains null pointers**
   - 仅用前序遍历（Preorder）就可以还原二叉树！😄
   - 仅用后序遍历（Postorder）也可以还原二叉树！✌️
   - 如果是中序遍历（Inorder），是无法还原二叉树的。😢

#### 2.6.3 Binary Search Tree (BST)

- For every node in a BST, the value of all nodes in its left subtree is less than the value of the node, and the value of all nodes in its right subtree is greater than the value of the node.
- All subtrees of a BST are also BSTs.
- BST 的中序遍历（inorder）结果是**升序**的。
- BST `containsKey()` runtime:
  - Perfectly balanced (best case): $`T(n)=\begin{cases}T(n/2)+1 & \text{if }n\gt 1\\ 3 & \text{otherwise}\end{cases} \\ T(n) = \Theta(\log n) \\ `$
  - Degenerate case (worst case): $`T(n)=\begin{cases}T(n-1)+1 & \text{if }n\gt 1\\ 3 & \text{otherwise}\end{cases} \\ T(n) = \Theta(n)`$

## 3. Arrays

### 3.1. Prefix Sum Algorithm

Prefix sum arrays are useful for *efficient and frequent* calculation of the *sum* of elements within a index range.

The idea is to store an array `preSum`, in which `preSum[i]` is the sum of `nums[0 ... i-1]`, which means that `preSum[i] = preSun[i-1] + nums[i]`. For example:

```python
      arr = [1, 2, 3,  4,  5]
preSum = [0, 1, 3, 6, 10, 15]
```

To find the sum of elements within the range `[1, 3]`, we can do the following:

- The sum of elements within the range `[1, 3]` is equal to `preSum[4] - preSum[1] = 9`

Example: [303. Range Sum Query](https://leetcode.cn/problems/range-sum-query-immutable/)

注意：前缀和数组比原input数组的size大一个。

### 3.2. Difference Array

Difference array is used for *fast, efficient* addition and subtraction of numbers within a range of indices. For example, add all numbers within range [0, 3] by 6, subtract all numbers within [2, 5] by 3, ..., etc. The idea is that, for every operation to add or subtract a number on all numbers within the range `[i, j]`, we only change the value of `diff[i]` and `diff[j+1]`, and then based on the result of diff array, find the result array.

`diff[i]` is the difference between `nums[i]` and `nums[i-1]`.

```python
diff = [0] * len(nums)
diff[0] = nums[0]
for i in range(1, len(nums)):
    diff[i] = nums[i] - nums[i - 1]
```

用差分数组迅速有效地进行区域中数字的加减，然后利用差分数组还原出`result`。比如想要`[i, j]`区间所有数字都+5，那么就把`diff[i] += 5`,`diff[j+1] -= 5`,然后还原结果。注意：差分数组和原input数组的size相等。

### 3.3. Sliding Window

The sliding window technique is used to solve *subarray* and *substring* problems.

Time complexity is usually O(N) because each element will only be added to window once and hence removed from window once (as `left` and `right` will never decrease).

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

Example Questions:

- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/), [solution](sliding_window/minimum_window_substring.py)

### 3.4. Binary Search on Arrays

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


### 3.5. Heap

In Python, use the `heapq` package to initialize and operate heaps.

```python
# Initialize heap
h = []

# Add element
heapq.heappush(h, (priority, element))

# Peek element
h[0]

# Pop element
priority, element = heapq.heappop(h)
```

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

### 8.2 Get ASCII Code of Characters

To get the ASCII code of a char: `ord(char)`

For example, `ord('A') = 65`

We can also do `ord('Z') - ord('A') = 25`. If we want to use an array of size 26 to store the count (or something else) of 26 upper case English characters, `ord(char) - ord('A')` will be the index of `char` in this array.

## 9. Interesting Problems

### 9.1. Selling and buying stocks

股票买卖问题都可以用 dynamic programming 的方法来解决。

#### Summary

#### Examples

- [题解及思路](dynamic_programming/README.md)
- [Solution to Problem 121. Best Time to Buy and Sell Stock](dynamic_programming/best_time_to_buy_and_sell_stock.py)
- [Solution to Problem 122. Best Time to Buy and Sell Stock II](dynamic_programming/best_time_to_buy_and_sell_stock_II.py)

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
