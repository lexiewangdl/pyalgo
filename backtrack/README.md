# Backtracking

## Table of Contents
- [216. Combination Sum III](#216-combination-sum-iii-medium) 🍊

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
