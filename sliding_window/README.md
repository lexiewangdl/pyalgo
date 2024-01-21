
# Sliding Window

The sliding window template: see [this page](../README.md).

## Table of Content
- [76. Minimum Window Substring](#76-minimum-window-substring-hard) 🍎
- [567. Permutation in String](#567-permutation-in-string-medium) 🍊
- [438. Find All Anagrams in a String](#438-find-all-anagrams-in-a-string-medium) 🍊
- [159. Longest Substring with At Most Two Distinct Characters](#159-longest-substring-with-at-most-two-distinct-characters-medium) 🍊
- [340. Longest Substring with At Most K Distinct Characters](#340-longest-substring-with-at-most-k-distinct-characters-medium) 🍊
- [187. Repeated DNA Sequences](#187-repeated-dna-sequences-medium) 🍊
- [209. Minimum Size Subarray Sum](#209-minimum-size-subarray-sum-medium) 🍊

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

### 340. [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) (Medium)
Same as above, except that when we check if a window needs to be shrinked, use `while len(window) > k` instead of `while len(window) > 2`.

### 187. [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) (Medium)
- Check every single possible substring of length 10, and store the substring in a set if it's not already in the set.
- Use a set to store duplicates, and return the list of duplicates at the end.

### 209. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) (Medium)
- Initialize `min_len` to be `math.inf`
- When returning the result, check if `min_len` is still `math.inf`, if so, return 0
- Use the sliding window template to solve this problem

### 424. [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium)
- Use the sliding window template to solve this problem
- To solve this question, we need to keep track of the following variables:
  - `max_count`: the maximum count of a single character in the current window
  - Then, we know that `len_window - max_count` is the number of characters that are not the most frequent character in the current window, which is the number of characters that need to be replaced
- Using the sliding window template, we keep track of two pointers `left` and `right`, and we keep expanding the window by incrementing `right` until `right` reaches the end of the string
- We use an array `window` to keep track of the count of each character in the current window
  - Initialize window: `window = [0 for _ in range(26)]`
  - Get the index of the current character: `index = ord(s[right]) - ord('A')` which is the same as `index = ord(s[right]) - 65`
- Every time we expand the window, update `max_count` in the following way: `if window[s[right]] > max_count: max_count = window[s[right]]`
- Then, we decide if the window needs to be shrinked: `if right - left + 1 - max_count > k:`
  - If so, we shrink the window by incrementing `left` and decrementing `window[s[left]]`
  - We also need to update `max_count` after shrinking the window: `max_count = max(window)`
- Finally, we update `max_len` every time we expand the window: `max_len = max(max_len, right - left + 1)`
- Return `max_len` at the end