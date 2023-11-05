# Graph Problems
This directory contains solutions to graph problems.

## Overview



## Table of Contents
- [277. Find the Celebrity](#277-find-the-celebrity-medium) 🍊

### [277. Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) (Medium)

The rule of celebrity: (1) everyone knows the celebrity, (2) the celebrity knows no one else.

#### Naive Solution (O(N^2))
Use nested for loops and use a data structure to keep track of number of people each person knows and number of people 
who know each person.

#### O(N) time, O(N) space Solution
Every time we call `knows(i, j)`, we eliminate one of the two people from being the celebrity.
If `i` knows `j`, then we know that `i` is not the celebrity. If `j` knows `i`, we know that `j` is not the celebrity.

Thus, we can use a queue to store all the people. Each time, we pop two people from the queue and call `knows(i, j)`.
Depending on the result, we can eliminate one of the two people from being the celebrity. We then push the remaining
person back into the queue. We repeat this process until there is only one person left in the queue.

When there is only one person left in the queue, we need to check if this person is the celebrity. We can do this by
checking if this person knows no one else and if everyone else knows this person.
If that's the case, return the index of this person. Otherwise, return -1.

#### Best Solution 💡 O(N) time, O(1) space
Use a integer `c` to keep track of the index of the celebrity. Initially, set `c = 0`.
Iterate through the rest of the people. If `c` knows `i` or `i` does not know `c`, then `c` is not the celebrity, but 
`i` could be the celebrity, so set `c = i`. Otherwise, `c` is still the celebrity.
Eventually, when we jump out of this loop, `c` will be the index of the last possible candidate! We just need to check
if `c` is the celebrity by checking if `c` knows no one else and if everyone else knows `c`.

Time complexity: O(2N) = O(N), using two for loops. Space complexity: O(1).


