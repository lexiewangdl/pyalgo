
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
- [487. Max Consecutive Ones II](#487-max-consecutive-ones-ii-medium) 🍊
- 🚩 [713. Subarray Product Less Than K](#-713-subarray-product-less-than-k-medium) 🍊

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

### 487. [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) (Medium)
Use a variable `flip_count` to keep track of the number of zeros that need to be flipped.

### 🚩 713. [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (Medium)
This problem is slightly different from the other sliding window problems because ...
- The window can be of size 1 (i.e. the window can be a single element)
- Must make sure that `l <= r` (i.e. the left pointer must be less than or equal to the right pointer)

It can be difficult to determine when to increment `l`. Here's the rule:
- (1) If the product of all elements in the window is less than `k` (`window_prod < k`), and
- (2) If `l <= r` (to take care of index out of range error),
- Then, we can increment `l` and update the product of all elements in the window.

Also, how many subarrays do we add to the result every time we increment `r`?
For example:
```python
nums = [10, 5, 2, 6]
k = 100
```
- When `r` is at index 0, we must add `[10]` to the result.
- When `r` is at index 1, we must add `[10, 5]` and `[5]` to the result.
- When `r` is at index 2, we must add `[5, 2]` and `[2]` to the result.
- When `r` is at index 3, we must add `[5, 2, 6]`, `[2, 6]`, and `[6]` to the result.

We can see that the number of subarrays we add to the result every time we increment `r` is equal to `r - l + 1`.
**Why is this the case?** 

The `+1` comes from the fact that we must add the subarray that contains only the element at index `r` (e.g. `[6]` when `r` is at index 3).
After the `while` loop used to increment `l`, `r` can either point to an element that's (1) less than `k` or (2) greater than or equal to `k`.
- If `r` points to an element that's less than `k`, then we must add the subarray that contains only the element at index `r` to the result.
  - e.g. `nums = [10, 5, 2, 6], r = 2, l = 0, k = 100`, value at index 2 is 2, which needs to be added to result
- If `r` points to an element that's greater than or equal to `k`, then `l` must be equal to `r + 1`, and `r - l + 1` will be equal to 0, so we don't need to add anything to the result.
  - e.g. `nums = [1, 1, 200, 1], r = 2, l = 3, k = 100`, value at index 2 is 200, which is greater than or equal to 100, 
    and `l` should be equal to `r + 1` after shrinking the window.

The `r - l` is equal to the number of subarrays of length >= 1 within the window that need to be added to the result.
For example, if the window is `[5, 2, 6]`, then we have two subarrays of length greater than 1 that need to be added to the result: `[5, 2, 6]` and `[2, 6]`.
Then we count the `+1` which will take care of `[6]`. Note that `[5, 2]` doesn't need to be counted because it would have been
counted already when `r` was pointing to `[2]`.

### 121. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy)
**When to enlarge the window?**
- Use `sell` variable to loop through the list `prices` starting from index `1`
- Increment `sell` by 1 every time

**When to shrink the window?**
- If `buy` price is higher than `sell` price, it means the `sell` day is a better day to buy in
- Thus, make `buy = sell` when `prices[sell] < prices[buy]`
- If we only increment `buy` by 1 when this condition is met, there will be bugs. This is because if the lower price (ideal buy in day) is toward the end of the array,
  `buy` might never get to that position before `sell` reaches the end of the array
