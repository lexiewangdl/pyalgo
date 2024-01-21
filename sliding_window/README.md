
# Sliding Window

The sliding window template: see [this page](../README.md).

## Table of Content
- [76. Minimum Window Substring](#76-minimum-window-substring-hard) 🍎
- [567. Permutation in String](#567-permutation-in-string-medium) 🍊
- [438. Find All Anagrams in a String](#438-find-all-anagrams-in-a-string-medium) 🍊
- [159. Longest Substring with At Most Two Distinct Characters](#159-longest-substring-with-at-most-two-distinct-characters-medium) 🍊

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

### 159. [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) (Medium)
The key point is to use `del dictionary[key]` to remove a key from a dictionary, this happens when we need to delete
characters from the window when the number of unique characters in the window is greater than 2.
