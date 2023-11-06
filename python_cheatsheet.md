# Python Cheat Sheet
This cheat sheet contains useful Python functions and data structures for solving LeetCode problems.

## Table of Contents
1. [Math](#1-math)
2. [String](#2-string)
3. [Queue](#3-queue)
4. Stack
5. [List](#5-list)


## 1. Math
1. Generate a random number in range [0, 1] (inclusive): `random.random()`
2. Generate a random integer in range [a, b] (inclusive): `random.randint(a, b)`
3. Floor division: `//`
4. Ceiling division: `math.ceil(x / y)`

## 2. String
1. Get ASCII code of a character: `ord('a')`
2. Compare strings: `str1 == str2`, `str1 < str2`, `str1 > str2`, etc.

## 3. Queue

Using `collections.deque` to implement a queue.
1. Initialize a queue: `q = collections.deque()`
2. Initialize a queue from list: `q = collections.deque([1, 2, 3])`
3. Add an element to the right of the queue: `q.append(4)`
4. Add an element to the left of the queue: `q.appendleft(0)`
5. Remove an element from the right of the queue: `q.pop()`
6. Remove an element from the left of the queue: `q.popleft()`
7. Check if queue is empty: `if not q:`
8. Get the size of the queue: `len(q)`

Useful links:
- [Python collections.deque() cheat sheet](https://cheatography.com/fidelp27/cheat-sheets/python-collections-deque/)

## 5. List
1. Sorting inplace: `list.sort()`
2. Sorting and return a new list: `sorted(list)`
3. Count the number of occurrences of an element in a list: `list.count(element)`
4. Initializing a list with a default value: `list = [0] * 10`
5. Initializing a matrix with a default value: `matrix = [[0] * n for _ in range(m)]`

