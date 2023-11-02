# Python Cheat Sheet

## Table of Contents
1. Math
2. String
3. Queue
4. Stack


## 1. Math
1. Generate a random number in range [0, 1] (inclusive): `random.random()`
2. Generate a random integer in range [a, b] (inclusive): `random.randint(a, b)`

## 2. String

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
