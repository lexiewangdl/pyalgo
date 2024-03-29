# Two Pointers

## Summary
Two pointers is a technique that involves using two pointers to solve a problem.
The time complexity of two pointers is usually **O(N)**, where N is the length of input array.

尤其适用于 input array or linked list 是 *sorted* 的情况。

### 双指针的三种类型

#### (1) 快慢指针 Slow and fast pointers, in the same direction
1. 环形链表：Detect cycle in linked list
2. 找链表中点：Find middle of linked list
3. 找链表中第n个元素：Find nth element in linked list
4. 删除重复元素：Remove duplicates from sorted array

#### (2) 对撞指针 Pointers that move in the opposite direction
1. 有序数组中两数之和：Two sum in sorted array
2. 检测回文串：Find palindrome 

#### (3) 分离指针 Pointers on different arrays
1. 两个有序数组的交集：Intersection of two sorted arrays
2. 合并有序数组：Merge two sorted arrays, aka. merge sort

### 细节处理

1. 两个指针的初始位置
   1. _快慢指针_：
      (1) 什么情况下快指针和慢指针都在最左边？
      (2) 什么情况下快指针和慢指针都在最右边？For example, in the case of [merging two sorted arrays](#88-merge-sorted-array-easy), both pointers start at the end of the array. This is because the end of the array is not populated, so we don't need to worry about overwriting elements.
      (3) 什么情况下快指针和慢指针在不同位置？For example, in a linked list, `left, right = None, head`, or in an array, `left, right = 0, 1`. This is useful when we want to _compare_ elements at different positions.
   2. 对撞指针：通常一个指针在最左边，一个指针在最右边
   3. 分离指针：通常两个指针都在最左边
2. 两个指针的移动条件

## Table of Contents
1. [26. Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array-easy) 🍏
2. [83. Remove Duplicates from Sorted List](#83-remove-duplicates-from-sorted-list-easy) 🍏
3. [27. Remove Element](#27-remove-element-easy) 🍏
4. [283. Move Zeroes](#283-move-zeroes-easy) 🍏
5. [167. Two Sum II - Input Array Is Sorted](#167-two-sum-ii---input-array-is-sorted-medium) 🍊
6. [344. Reverse String](#344-reverse-string-easy) 🍏
7. [5. Longest Palindromic Substring](#5-longest-palindromic-substring-medium) 🍊
8. [121. Best Time to Buy and Sell Stock](#121-best-time-to-buy-and-sell-stock-easy) 🍏
9. [443. String Compression](#443-string-compression) 🍊
10. 🚩 [42. Trapping Rain Water](#42-trapping-rain-water-hard) 🍎
11. 🚩 [11. Container With Most Water](#11-container-with-most-water-medium) 🍊
12. [88. Merge Sorted Array](#88-merge-sorted-array-easy) 🍏
13. 🚩 [80. Remove Duplicates from Sorted Array II](#80-remove-duplicates-from-sorted-array-ii-medium) 🍊

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

### 27. Remove Element (Easy)
**My solution**:

Use two pointers `i` and `j`.

`j` is the number of elements in array that is not equal to val, which is also the index
where the next unequal element should be placed at. The initial value of `j` is `0` because 
the list is not sorted, and element at any index could be equal to `val`.

`i` is what we use to loop through the array with a `for` loop. It checks the value at index `i`, if `nums[i]` is equal to `val`, 
we do nothing, which means `i` gets incremented by 1, whereas `j` remains unchanged. If `nums[i] != val`, it means that we have found
an element that's NOT equal to `val`, and this element needs to be placed at index `j`.

Note that `j` only gets incremented after a swap happens. 
There are two scenarios in which a swap happens: (1)
`i` and `j` are equal (pointing to same element), in this case, a swap doesn't change anything. 
We can understand this to be `j` gets incremented when element at `j` is not equal to `val`.
(2) `i` and `j` are not equal. For a swap to happen, `i` must be pointing to an element that is NOT equal to `j`, and for `j`
to be not equal to `i`, `j` must be pointing to an element that's equal to `val` (since `i` only increments without `j` if `nums[i] == val`)

### 283. Move Zeroes (Easy)
**My solution:**

Very similar to previous problem.

`j` represents the index where next non-zero element should be placed. All elements to the left of `j` are non-zero.

`i` is used to loop through the array with a `for` loop. If `nums[i] != 0`, swap with `nums[j]`.


Different from last problem: in last problem, we only care about the first `j` elements in array, all elements from index `j` onwards
are not important, so when we swap, we are not necessarily swapping, it's just setting element at `j` to be equal to element at `i`.
In this problem, elements need to be actually swapped.

### 167. Two Sum II - Input Array Is Sorted (Medium)
**My solution**:

Use a *sliding window* approach.

Since the input array is sorted in non-descending order, smaller elements are to the left and larger elements are to the right.
Use two pointers `l` and `r`, `l` starts at index `0` and `r` starts at index `len-1`. Shrink the window gradually as we approach the answer.

If `nums[l] + nums[r] == target`, we have found the answer, return the answer. Otherwise, if `nums[l] + nums[r] > target`,
we know that we must shrink the window by decrementing `r` to reduce the sum. If `nums[l] + nums[r] < target`, we know that
the element pointed to by `l` is too small, must increment `l` to increase sum.

### 344. Reverse String (Easy)

Left and right pointers. Initialize `l = 0` and `r = len(s) - 1`, swap `l` and `r` at every step, increment `l` and 
decrement `r` simultaneously, stop when `l >= r`

### 5. Longest Palindromic Substring (Medium)

This question can be divided into two parts:
(1) How to find the longest palindrome given an index in string? (2) Check for indices in string.

(1) How to find the longest palindrome given an index in string?

Start at the middle index of the string, use two pointers `l` and `r` and gradually expand the window while the following 
criteria are satisfied: `l >= 0`, `r <= len(nums)`, and `s[l] == s[r]`.

(2) We need to check all substrings. However, we don't want to actually check all possible substrings.
Thus, we can find the longest palindrome for every single index.
There are two scenarios: (1) the longest palindrome has odd-numbered length, e.g. "aba", in this case,
the starting values of `l` and `r` (for previous sub-task) are both equal to `i`. (2) the longest palindrome has even-numbered
length, in this case, `l` and `r` should be `i` and `i+1`.

### 121. Best Time to Buy and Sell Stock (Easy)

Use two pointers `l` and `r`, `l` starts at index `0` and `r` starts at index `1`.
Use a while loop (`while r < len(arr):`) to iterate through the array, at each step, do the following: (1)
If current profit is greater than 0, it means that we can make a profit by buying at `l` and selling at `r`, so we check
whether current profit is greater than `max_profit`, if so, update `max_profit`. (2) If current profit is less than 0,
it means that `prices[l]` is greater than `prices[r]`, so we should set `l` to be equal to `r`. Note that we can't
just increment `l` by 1, because we don't know whether `prices[r]` is the smallest element in the array, so we need to
set `l` to be equal to `r` to ensure that `prices[l]` is the smallest element in the array.
In other words, we are trying to find the smallest element in the array, and we want `l` to be pointing to that element.
If we find an element that is smaller than `prices[l]`, we set `l` to point to that element.
(3) Increment `r` by 1, at every step.


### 443. String Compression
Use two pointers `l` and `r`, `l` starts at index `0` and `r` starts at index `1`.
Use two variables `curr_char` and `curr_count` to keep track of current character and current count.
Use a while loop (`while r < len(arr):`) to iterate through the array, at each step, do the following: 
1. If `arr[r] == curr_char`, increment `curr_count` by 1. 
2. If `arr[r] != curr_char`, we have found a new character, so ...
   1. Update resulting array: 
      1. set `arr[l]` to be equal to `curr_char`, increment `l` by 1.
      2. set `arr[l+1]` to be equal to `curr_count`. Note that if count is more than 10, for example "12", it will need 
         to be stored as two separate characters, "1" and "2", so we need to convert `curr_count` to a string, and then
         use a for loop to iterate through the string and set `arr[l]` to be equal to each character in the string,
         and increment `l` by 1 at every step.
   2. Update `curr_char` and `curr_count`:
      1. set `curr_char` to be equal to `arr[r]`
      2. set `curr_count` to be equal to `1`
   3. Increment `r` by 1, at every step.
3. After the while loop, we need to update the resulting array one last time. 
   This is because the while loop only updates the resulting array when `arr[r] != curr_char`,
    but if `arr[r] == curr_char` at the end of the while loop, we need to update the resulting array one last time.

Note: `l` is the index where next processed element should be placed at, it is also the length of the
resulting array.

Time complexity: O(N), Space complexity: O(1)

### 42. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/) (Hard)

重点：不要去想整体能装多少水，先去想在每个位置`i`上能装多少水。
位置`i`能装多少水取决于左侧和右侧最高的柱子的高度，即`max_left`和`max_right`。
所以位置`i`能装多少水取决于`min(max_left, max_right) - height[i]`。

**Two pointers solution**: [trapping_rain_water.py](trapping_rain_water.py)
- Initialize `left = 0`, `right = len(height) - 1`
- Keep track of `l_max` and `r_max`, where `l_max` is the maximum height of all bars to the left of `left` pointer,
  and `r_max` is the maximum height of all bars to the right of `right` pointer
  ```shell
  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
         ^                    ^
         l                    r
  l_max = 1
  r_max = 2
  ```
- Use a while loop `while left < right`, make two pointers move in opposite directions
- The question is: when do we move `left` pointer and when do we move `right` pointer?
  - 当`left`指针和`right`指针相遇之前，`l_max`一定是`left`左边最高的bar的高度。但是，`r_max`不一定是`left`右边最高的bar的高度。
  - 这是因为`left` and `right`中间还有一段位置没有见过。
  - 但是，我们并不在乎`r_max`是不是`left`右边最高的bar，因为`height[i]`位置能够取的水量取决于最低的那个bar，也就是`min(l_max, r_max)`。
  - 接下来，我们要决定移动`left`还是移动`right`。
  - 如果`l_max < r_max`，那么`height[left]`能够取的水量取决于`l_max`，这个时候我们已经算完了`height[left]`的水量，所以我们移动`left`。
  - 如果`l_max >= r_max`，那么`height[right]`能够取的水量取决于`r_max`，这个时候我们已经算完了`height[right]`的水量，所以我们移动`right`。
  - At every step, we only move one pointer, and we only move the pointer on the side that has the smaller maximum height.

### 11. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium)
Similar to previous question, use **two pointers** ([solution](container_with_most_water.py)). Initialize `left = 0` 
and `right = len(height) - 1`. Keep track of maximum bar height to the left of `left` pointer and maximum bar height
to the right of `right` pointer, using `l_max` and `r_max` respectively. 
Use a while loop `while left < right`, make two pointers move in opposite directions.
At every step, update `l_max` and `r_max` first, and then, compare `l_max` to `r_max`, because the amount of water
we can store in between `left` and `right` is determined by the smaller of the two maximum bar heights.
If `l_max < r_max`, increment `left` by 1, otherwise, decrement `right` by 1.

### 88. [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) (Easy)
Use **two pointers** ([solution](merge_sorted_array.py)). Initialize `p1 = m - 1` and `p2 = n - 1`, where `m` is the length
of `nums1` and `n` is the length of `nums2`. Use a while loop `while p1 >= 0 and p2 >= 0`, at every step, compare `nums1[p1]` and `nums2[p2]`.
If `nums1[p1] > nums2[p2]`, set `nums1[p1 + p2 + 1]` to be equal to `nums1[p1]`, and decrement `p1` by 1. Otherwise, set `nums1[p1 + p2 + 1]` to be equal to `nums2[p2]`, and decrement `p2` by 1.
After the while loop, if `p2 >= 0`, it means that there are still elements in `nums2` that haven't been processed, so we need to copy these elements to `nums1`.

The key is to move from the back of `nums1` and `nums2`, and compare elements at `p1` and `p2` at every step, as the back of
the array is not populated. When we get to the populated parts, we don't need to worry about overwriting elements because
we have already processed them.

### 🚩 80. [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) (Medium)
Initialize `left = 0` and `right = 1`. Use a while loop `while right < len(nums)`, at every step, compare `nums[left]` and `nums[right]`.
If `nums[left] == nums[right]`, increment `right` by 1. Otherwise, increment `left` by 1, and set `nums[left]` to be equal to `nums[right]`.
Note that `left` must be incremented by 1 before setting `nums[left]` to be equal to `nums[right]`, because we want to keep the first two occurrences of a number, and we want to overwrite the third occurrence of the number.
After the while loop, return `left + 1`.
