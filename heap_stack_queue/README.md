# Heap, Stack, and Queue

## Table of Contents
1. [Heap Summary](#heap-summary)
2. [Heap in Python](#heap-in-python)
3. [Heap Problems](#heap-problems)
4. [Queue Summary](#queue-summary)
5. [Queue in Python](#queue-in-python)
6. [Queue Problems](#queue-problems)


## Heap Summary

| Operation        | Best Case | Average Case | Worst Case |
|------------------|-----------|--------------|------------|
| Insertion        | O(1)      | O(log N)     | O(log N)   |
| Deletion         | O(1)      | O(log N)     | O(log N)   |
| Search           | O(1)      | O(N)         | O(N)       |
| getMax (MaxHeap) | O(1)      | O(1)         | O(1)       |
| getMin (MinHeap) | O(1)      | O(1)         | O(1)       |

- Insertion
  - Best case O(1) when (in min heap) inserted value is greater than it's parent
  - Average and worst case O(log N) because we need to shift inserted value until we reach the root (or heap invariant restored)
- Deletion
  - Worst and average case O(log N) because downshift till bottom of heap (or heap invariant restored)
- Search
  - Best case O(1) when element to search is the root node
  - Worst case O(N) only find element at very end of search

## Heap in Python
1. Initialize a heap: `heap = []`
2. Insert an item into a heap: `heapq.heappush(heap, (priority, item))`
3. Pop the smallest item from a heap: `heapq.heappop(heap)`
4. Everything stored in heap must be **comparable**. If a tuple is pushed, the first item is used for comparison. If two tuples have the same first item, the second item is used for comparison, and so on, both items in tuple must be comparable.

```python
import heapq

heap = []
heapq.heappush(heap, (2, 2))
heapq.heappush(heap, (1, 3))  # (frequency, number)

print(heapq.heappop(heap)) # (1, 3)
```
## Heap Problems
- 🚩 [347. Top K Frequent Elements](#347-top-k-frequent-elements-medium) 🍊
- [23. Merge k Sorted Lists](#23-merge-k-sorted-lists-hard) 🍎
- 🚩 [295. Find Median from Data Stream](#295-find-median-from-data-stream-hard) 🍎
- [215. k-th Largest Element in an Array](#215-kth-largest-element-in-an-array-medium) 🍊
- 🚩[2462. Total Cost to Hire K Workers](#2462-total-cost-to-hire-k-workers-medium) 🍊
- 🚩 [658. Find K Closest Elements](#658-find-k-closest-elements-medium) 🍊
- [272. Closest Binary Search Tree Value II](#272-closest-binary-search-tree-value-ii-hard) 🍎

### 347. Top K Frequent Elements (Medium)
1. Use `Counter()` to get the frequency of each element in the list.
2. Store each number and its corresponding frequency in a `heap`. Note: since this heap is a min heap, and what we want is the top k frequent elements, we need to store the negative frequency of each element in the heap, `heappq.heappush(heap, (-freq, num))`. In this way, we have a max heap.
3. Pop the top k elements from the heap, `heapq.heappop(heap)[1]`.


### 23. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/) (Hard)
Use one priority queue (heap) to store the first node in each linked list.
The priority is determined based on the node's value.

While the heap is not empty, pop the element with smallest priority (value) from the heap. Then connect this node
to the result linked list. If this node has a next node, push the next node into the heap.

Time complexity: **O(N log k)**
- The _log k_ comes from pushing and popping from heap, since the heap will only contain _k_ elements at max, time complexity for pushing and popping are both O(log k)
- The _N_ comes from the while loop `while heap is not empty`. Heap will only become empty when every single node has been added and popped, and there are _N_ nodes in total

### 295. [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard)
Use two heaps:
- `max_heap` is used to store elements in left half of sorted data array
- `min_heap` is used to store elements in right half of sorted data array

**Why?** In this way, we can easily get the median of all data points. 
If total number of elements is **even numbered**, we can access the max element in `max_heap` and the min element
in `min_heap` and take average of the two.
If the total number of elements is **odd numbered**, we can just get the min element in `min_heap`.

**Invariants to maintain:** to achieve the goals above, we must maintain the following invariants:
- If the total number of elements is _n_, then ...
- The length of left half (`max_heap`) is always _n/2_
- The length of right half (`min_heap`) is always _n/2_ or _n/2 + 1_

Thus, if the left half has length _k_, right half will have length _k_ or _k+1_.

**Adding element:** Make sure we maintain the invariants as we add elements.
- If the current lengths are (k, k), we want the lengths of two heaps to become (k, k+1), with the `min_heap` having one more element
- However, we can't just put the new element into `min_heap`! We want to make sure that elements are sorted in order, so we push the element into `max_heap` first, and then pop the max element from `max_heap` to put it in `min_heap`
- If current lengths are (k, k+1), we want the lengths to become (k+1, k+1). However, we can't just put the new number in `max_heap`. Same idea, push into `min_heap` first and then pop the minimum element from `min_heap` and put it in `max_heap`

For example:
```bash
max_heap        min_heap
[3, 2, 1]       [5, 6, 7]

>> addNum(4)

Step 1: heappush(max_heap, 4)
[4, 3, 2, 1]       [5, 6, 7]
Step 2: n = heappop(max_heap)  (n = 4)
[3, 2, 1]       [5, 6, 7]
Step 3: heappush(min_heap, n)
[3, 2, 1]       [4, 5, 6, 7]
(len = 3)       (len = 3 + 1)
```

**Finding the median**:
- If lengths of two heaps are equal, get the max element from `max_heap` and min element from `min_heap` and find average
- Otherwise, get min element from `min_heap`
- Note: don't use `heappop()` here because we don't want to remove the elements from the heaps! Just use `min_heap[0]` and `-max_heap[0]` to get the elements

**Max heap in Python:** To maintain a max heap, just use a negative sign whenever we add and pop elements into and from a max heap.
- Add to max heap: `heappush(max_heap, -num)`
- Pop from max heap: `-heappop(max_heap)`
- Get max value from max heap: `-max_heap[0]`

### 215. [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium)

[Python solution](kth_largest_element_in_array.py):

Maintain a single **heap** of size _k_. This heap stores the _k_ largest elements in the processed array.
For example, the array `nums` is `[1, 2, 3, 4, 5]`, and `k = 2`. 

We use a for loop to iterate through the array. For each element, we do the following:
1. Push the element into the heap
2. If the heap size is greater than _k_, pop the smallest element from the heap (so that the heap size is always _k_, and always contains the _k_ largest elements in the processed part of the array)

At the end of the loop, the heap will contain `[4, 5]`.
The top element of the heap is the _k_-th largest element in the array.

**Time complexity**: O(N log k)

The for loop iterates through the array, which is O(N), 
and each iteration takes O(log k) time to push and pop elements from the heap.

### 2462. [Total Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) (Medium)

[Python solution](total_cost_to_hire_k_workers.py):

This problem needs to find the minimum cost to hire _k_ workers. For each hiring session, we need to hire exactly _1_ worker.
There will be _k_ hiring sessions in total.

For each session, the candidates are the workers from the first `candidates` in `costs` (which defines the cost of hiring each worker at corresponding index) to the last `candidates` in `costs`. 
For example, if `costs` is `[1, 2, 3, 4, 5]`, and `candidates = 2`, then 
the candidates for the first session are `[1, 2]` and `[4, 5]`.
Note that **each person can only be hired once**, so if `candidates = 3`, then in the first session,
the candidates are `[1, 2, 3]` and `[4, 5]`.

The approach is to initialize two heaps:
- `l_heap` is used to store the candidates from the first `candidates` in `costs`
- `r_heap` is used to store the candidates from the last `candidates` in `costs`

Using a for loop `for i in range(k):` to iterate through the hiring sessions.

For each session, we do the following:
1. Use a `while` loop to add the candidates from the first `candidates` in `costs` to `l_heap` until the size of `l_heap` is `candidates`
2. Use a `while` loop to add the candidates from the last `candidates` in `costs` to `r_heap` until the size of `r_heap` is `candidates`
3. After the `while` loops, we have two heaps, `l_heap` and `r_heap`, each with size `candidates`.
4. Compare the top elements of the two heaps. The heap with the smaller top element is the heap that contains the candidates with the lowest cost. Pop the top element from this heap and add it to the `total_cost`. (Note that if a heap is empty, we can't pop from it. So we need to check if the heap is empty before popping from it.)

### 658. [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) (Medium)
The input array is in ascending order, and there is a target value. We need to find the _k_ closest elements to the target value
in the array, and return them in ascending order.
It's important to note that this target value may or may not be in the array.

It makes sense to use **binary search** for this problem, but it's actually a lot easier to use **heap**.

- Store every single element in `arr` into a heap, with the priority being the absolute difference between the element and the target value `abs(arr[i] - x)`.
- The elements in heap will be ordered by the priority, so we can just pop the top _k_ elements from the heap and store them in a list.
- Sort the list and return it.

### 272. [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) (Hard)
Use a global variable `heap` to store the binary tree values.
Use a helper function `dfs()` to traverse the tree in order, and add the current node's value to the heap.
When adding the current node's value to the heap, we need to store priority as the absolute difference between the current node's value and the target value `abs(node.val - target)`: `heapq.heappush(heap, (abs(node.val - target), node.val))`.
Finally, pop the top _k_ elements from the heap and return them: `result = [heapq.heappop(self.heap)[1] for _ in range(k)]`.


## Stack Problems
- [20. Valid Parentheses](#20-valid-parentheses-easy) 🍏
- [32. Longest Valid Parentheses](#32-longest-valid-parentheses-hard) 🍎

### 20. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy)
Solution:
- Use a stack to store the opening parentheses: `stack = []`
- Use a `for` loop to iterate through the string.
- For each element, if it is an opening parenthesis, push it into the stack.
- If it is a closing parenthesis ...
  - If the stack is empty, return `False` (this means that either we have never encountered an opening parenthesis, or all previous opening parentheses have been closed/matched)
  - Otherwise, compare the top element from the stack and check if it matches the current closing parenthesis. 
    - If it doesn't match, return `False`.
    - If it matches, pop the top element from the stack.
- If the stack is empty after the loop, return `True`.

### 32. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) (Hard)

## Queue Summary
Queue is a FIFO data structure. It's like a line of people waiting to get into a concert. The first person in line is the first person to get into the concert. It is commonly used in BFS (e.g. level-order traversal of binary tree).

## Queue in Python
```python
queue = []

# enqueue
queue.append(item)

# dequeue
queue.pop(0)
```

## Queue Problems

