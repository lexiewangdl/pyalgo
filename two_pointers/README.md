# Two Pointers


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

