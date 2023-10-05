# Array Problems

## Table of Contents
- 704 - Binary Search 🍏
- 34 - Find First and Last Position of Element in Sorted Array 🍊
- 528 - 🚩 Random Pick with Weight 🍊

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
