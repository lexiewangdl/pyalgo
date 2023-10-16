# Heap, Stack, and Queue

## Table of Contents
1. [Heap Summary](#heap-summary)
2. [Heap in Python](#heap-in-python)
3. [Heap Problems](#heap-problems)


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
- 347 - 🚩 [Top K Frequent Elements](#347-top-k-frequent-elements--medium-) 🍊
- 23 - [Merge k Sorted Lists](#23-merge-k-sorted-lists--hard-) 🍎


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


## Stack Problems

## Queue Problems

