# Array Problems

## Table of Contents
- 76 - 🚩 Minimum Window Substring 🍎
- 567 - Permutation in String 🍊
- 438 - Find All Anagrams in a String 🍊
- 704 - Binary Search 🍏
- 34 - Find First and Last Position of Element in Sorted Array 🍊
- 528 - 🚩 Random Pick with Weight 🍊
- 380 - Insert Delete GetRandom O(1) 🍊
- 347 - 🚩 Top K Frequent Elements 🍊

### 76. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard)
For template of sliding window questions, see [this page](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md).

Key points:
- Must use `valid` (in this case, I used `count`) to store the number of keys whose value in `window` is greater than or equal to in `need` (I used `t_map`), this is because when comparing two dicts directly, it won't take care of situations where the values in `window` are greater than in `need` (e.g. `window = {'A': 2, 'B': 1}` and `need = {'A': 1, 'B': 1}`)
- Even though `right` is initialize to be zero, it's always incremented right after the corresponding character is saved in a variable. When we exit the outer while loop, right will be equal to `len(s)`. Thus, the range is actually `[left, right)` (the right index is non-inclusive).
- This is why the returned result is `s[left:right]` (this is a simplified way of representing it, refer to code for edge case handling)
- Only save char in `window` if char is a needed char (save some space)

### 567. [Permutation in String](https://leetcode.com/problems/permutation-in-string/) (Medium)
Use the [sliding window template](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md).

### 438. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/) (Medium)
Use the [sliding window template](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md).


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
See [this page](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md) for binary search template.

Basically, do binary search once to find the left-most target, and search again to find 
the right-most target.

### 528. [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/description/) (Medium)

Key skills: preSum array, binary search

题目给出的数组`w` 是每个index被选中的对应的weight，比如`w = [1, 3]`，index 0被选中的概率是1/4，index 1被选中的概率是3/4。

Python自带的生成随机整数的方法`random.randint(a, b)`是在range [a, b]（闭区间）之内随机生成一个整数，并不是根据每个值被选中的weight来选择。如何将这个function运用到这道题目中呢？

使用前缀和数组`preSum`则可以做到这件事。从`w`构建前缀和数组，`preSum = [0, 1, 4]`，然后使用`randint(1, 4)`在range`[1, 4]`之间随机选取一个数。一共有以下几个数字可能被选到：1，2，3，4，其中如果1被选到，则对应着前缀和数组中的index 1，如果2，3，4被选到，则对应着前缀和数组中index为2，这样的话，相当于选到index 2的概率为3/4，也正是我们想要的结果。

需要注意的是，`randint()` 选择的range是`[1, preSum[n-1]]`，而n则是前缀和数组的长度。这个range必须从1开始，而不是从`preSum[1]`开始，因为如果`preSum[1]`不等于1，举例来说如果是3，那么选择到1，2，3这三个数字中的任意一个，都代表我们选到了3。如果range是从3开始，那么我们不再又可能选到1和2，那么选到3这个数字的概率就不对了。

另外一个问题是，使用`randint()`生成range中的随机整数后，如何找到这个结果在前缀和数组中对应的index呢？这个时候需要用到搜索算法。但首先我们需要知道我们要搜索的结果是什么。假设我们选定的数字为x，如果x存在在前缀和数组之中，那么我们只需要返回x在前缀和数组中的index。另一种可能是，x不存在在前缀和数组之中，不过我们知道的是，x被选到也就代表着前缀和数组中大于x的最小的数字所在的index被选中（参考2，3被选中时，其实选中的是`preSum`中的4，也就是index 2）。所以我们的**搜索目标**是`preSum`中x的index或大于x的最小元素的index。

这个目标可以用二叉搜索（左边界）实现。搜索左边界的二叉搜索，如果数组中不存在等于target的值，则会返回比target大的第一个元素所在的index，也可以用以下方式理解，左边界二叉搜索返回的index为...

- 数组中大于等于`target`的最小元素的index
- 此index为`target`应该插入在数组中的位置
- 此值为数组中小于`target`的元素的个数

比如输入为`nums = [0, 3, 17, 18, 25]`，要找的数字为10，最后退出while loop的时候左右指针都会指向17，也就是index为2。如果数字10需要insert到数组中，它就会出现在index 2的位置。同时，数组中小于10的数字一共有两个。

### 380. [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/) (Medium)
1. How to get a random element in a data structure in O(1) time?

    If we have an **array**, we can use `random.randint()` to generate a random index within the range (0, len(array)-1). Then we can return the element at that index.
    We can also just use `random.choice(array)` to get a random element in the array.
2. How to insert and delete an element in a data structure in O(1) time?

    If we have a **hash table**, we can insert and delete an element in O(1) time. However, we cannot get a random element in O(1) time.
    If we have an **array**, we can still insert and delete in O(1) time, as long as the item is added to the end or removed from the end.
3. How to make sure that the item to delete is at the end of the array?

   Swap the item to be deleted with the last item in the array, and then delete the last item in the array.
4. Swap items in O(1) time?

   Use a hash table to store the index of each item in the array. In this way, we can find the **index of item to delete** in O(1) time and swap it with the last element in list in O(1) time.
5. Other key points: (1) remember to increment data length when inserting an item; (2) remember to decrement data length when deleting an item; (3) remember to update the hash table when swapping items.

### 347. Top K Frequent Elements (Medium)
1. Use `Counter()` to get the frequency of each element in the list.
2. Store each number and its corresponding frequency in a `heap`. Note: since this heap is a min heap, and what we want is the top k frequent elements, we need to store the negative frequency of each element in the heap, `heappq.heappush(heap, (-freq, num))`. In this way, we have a max heap.
3. Pop the top k elements from the heap, `heapq.heappop(heap)[1]`.

### Heap in Python
1. Initialize a heap: `heap = []`
2. Insert an item into a heap: `heapq.heappush(heap, (priority, item))`
3. Pop the smallest item from a heap: `heapq.heappop(heap)`

