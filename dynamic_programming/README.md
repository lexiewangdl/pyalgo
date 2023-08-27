# Dynamic Programming
**Table of Contents**
- 509 Fibonacci Number

### 509. Fibonacci Number
Given two base cases `f(0) = 0` and `f(1) = 1`, we know that for all other values of `n`, `f(n) = f(n-1) + f(n-2)`.
Thus, we know that the value of `f(n)` only depends on the values `f(n-1)` and `f(n-2)`.

Store the value of these two numbers, update at every step (after current f(n) has been calculated). No need to use an array
to store all numbers that we calculated in previous steps.

Time complexity: O(n), Space complexity: O(1)
