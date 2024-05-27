# Backtracking

## Table of Contents
- [216. Combination Sum III](#216-combination-sum-iii-medium) 🍊
- 元素无重，不可复选：
- 元素有重，不可复选：
  - 子集：[90. Subsets II](#90-subsets-ii-medium) 🍊
- 元素无重，可复选：


### 90. [Subsets II](https://leetcode.com/problems/subsets-ii/description/) (Medium)
子集问题，元素有重复，不可以复选。

**不可以重复选择同一个元素**，意味着需要用`start`变量，来记录接下来可以选择的元素的起始位置。这个方法有两个作用：
1. 避免选择同一个元素多次
   - 比如`nums = [1, 2]`，当在`[1]`的节点发展分支时，下一个可以选择的元素只能是`2`得出`[1,2]`，而不能再选择`1`，意味着`[1,1]`不是合法答案。
2. 避免出现同一个子集的不同排列
   - 在`[2]`节点发展树枝时，我们不会再看`1`，因为`[1,2]`已经在`[1]`节点时被考虑过了。
      这个时候再加入`[2,1]`就是重复的了。

具体的方法是，`backtrack()`函数有一个参数为`start`，意味着在这个节点开始发展分支，index为`start`及之后的元素都可以被选择。
当我们在`for`循环中，使用`for i in range(start, len(nums))`，就可以实现上述的目的。
在进入下一层递归时，`start`的值就是`i+1`，意味着下一层递归的`for`循环中，只能选择`i+1`及之后的元素，因为`i`已经被选择过了。

**元素有重复**，意味着有可能出现的情况是，多个不同的元素组成的子集是重复的。比如`nums = [1, 2, 2]`， `[1,2]`（第一个2）和`[1,2]`（第二个2）是重复的。
所以我们需要对回溯树??进行剪枝（pruning），避免出现重复的子集。

具体的方法是，在`for`循环中，如果当前元素与同一层的前一个节点所选择的元素相同，我们就跳过这个元素。比如在`[1]`, `[2]`（第一个2）节点已经处理过后，
不需要再用第二个2再次处理`[2]`。
但是如果是在不同层选择值想等的元素，是不能剪枝的。比如在`[1,2]`节点，还是要继续选择2去得到`[1,2,2]`。
我们要检查的是`i > start`，因为`i == start`时，位置`i`的元素是这一层可以选择的第一个元素，不需要剪枝。

```python
def backtrack(start, path):
    # Add path to result
    result.append(path)

    for i in range(start, len(nums)):
        # Pruning
        if i > start and nums[i] == nums[i-1]:
            continue
            
        # Recurse
        backtrack(i+1, updated_path)
        ...
```

更重要的是，如果`nums`没有**排序**，我们需要先对`nums`进行排序，这样才能保证相同的元素都在一起，方便剪枝。


### 216. [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) (Medium)
Use backtracking to find all combinations of `k` numbers that add up to a number `n`, given that only numbers from `1` to `9` can be used and each combination should be a unique set of numbers.

To define the recursive function, we need to know the following:
1. What are the arguments?
   1. The current combination `track` that we are building, for example, if we already have `[1, 2]` and we are looking for a third number so that 3 numbers sum up to 7, `[1, 2]` is the current track
   2. The choices that we have, in this case, the numbers from `1` to `9`, we don't need to store the choices using a separate variable because we can simply use a for loop.
   3. The target number `n`, which is the sum that we are looking for. If not passed, we can also keep track of the remaining sum `remain` and pass that as an argument.
   4. The number of numbers that we are looking for, `k`. 
2. What does the function return? The return type of the function is usually `None` for backtracking.
3. What is the base case?
   1. When the sum of numbers in `track` is equal to `n`, and the length of `track` is equal to `k`, we have found a valid combination, so we add `track` to the result.
   2. If the length of the track is equal to `k` but the sum is not equal to `n`, we have found a combination but it's not valid, so we return, there is no need to continue working on current track.
4. What is the recursive case?
    1. Use a for loop to iterate through the choices, which are the numbers from `1` to `9`.
   2. To simplify this process, we can use a variable `start` to keep track of the smallest number that we can use in the current track. 
   3. This is because the questions requires that the same combination should not be added multiple times. Since our for loop goes in ascending order, when see the combination `[4, 1, 2]`, we know for sure that `[1, 2, 4]` must already been added to the result. 
   4. Thus, we can use `start` to keep track of the smallest number that we can use in the current track. `start` would be 1 if the track is empty, and it would be the last number in the track plus 1 `track[-1] + 1` if the track is not empty.


### 79. [Word Search](https://leetcode.com/problems/word-search/) (Medium)
- 元素有重，不可复选

- Use backtracking to find if a word exists in a 2D board.
- Use a matrix `used` or modify `board` to mark the cells that have been visited.
  - e.g. `board[i][j] = '#'`, undo the change after the recursive call.
- The recursive function should have the following arguments:
  1. The current position `(i, j)` that we are at.
  2. The current index `idx` of the character in the word that we are looking for.
- Base cases:
  1. `idx`: If `idx` is equal to the length of the word, we have found the target word in the `board`.
  2. Check if we have found the target using `self.found` flag. If we have found the target, we can return immediately.
  3. Check if the current position `(i, j)` is out of bounds.
  4. Check if the current character in the `board` is not equal to the character in the word at index `idx`.
  5. Check if the current position `(i, j)` has already been visited.
  6. If all the above conditions are met, we can mark the current position as visited and recursively call the function for the neighboring cells.

我们要在`board`上找到`word`，所以就是只需要找到一个长度为`len(word)`的路径，这个路径上的字符依次组成`word`即可。
也就是说，这个路径上每个`char`都是`word`中的一个字符，且相邻的字符在`word`中也是相邻的。

