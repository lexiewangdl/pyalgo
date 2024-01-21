
# Sliding Window

## Table of Content
- [76. Minimum Window Substring](#76-minimum-window-substring-hard)
- [567. Permutation in String](#567-permutation-in-string-medium)
- [438. Find All Anagrams in a String](#438-find-all-anagrams-in-a-string-medium)
- [380. Insert Delete GetRandom O(1)](#380-insert-delete-getrandom-o1-medium)
- [268. Missing Number](#268-missing-number-easy)
- [1306. Jump Game III](#1306-jump-game-iii-medium)
- [36. Valid Sudoku](#36-valid-sudoku-medium)

## Questions and Solutions

### 76. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard)
For template of sliding window questions, see [this page](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md).

Key points:
- Must use `valid` (in this case, I used `count`) to store the number of keys whose value in `window` is greater than or equal to in `need` (I used `t_map`), this is because when comparing two dicts directly, it won't take care of situations where the values in `window` are greater than in `need` (e.g. `window = {'A': 2, 'B': 1}` and `need = {'A': 1, 'B': 1}`)
- In other words, `valid` represents the number of elements in current window that have satisfied the requirement in `need` (i.e. greater than or equal to the needed count)
- Even though `right` is initialized to be zero, it's always incremented right after the corresponding character is saved in a variable. When we exit the outer while loop, right will be equal to `len(s)`. Thus, the range is actually `[left, right)` (the right index is non-inclusive).
- This is why the returned result is `s[left:right]` (this is a simplified way of representing it, refer to code for edge case handling)
- Only save char in `window` if char is a needed char (save some space), and only remove char from window if char is a needed char.

### 567. [Permutation in String](https://leetcode.com/problems/permutation-in-string/) (Medium)
Use the [sliding window template](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md).

### 438. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/description/) (Medium)
Use the [sliding window template](https://github.com/lexiewangdl/pyalgo/blob/2f0446458ce2647cca671149926d3492e395ad48/README.md).

