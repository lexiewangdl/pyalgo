# Graph Problems
This directory contains solutions to graph problems.

## Overview
* A **graph** consists of a set of **nodes** and a set of **edges**. 
* Each edge connects two nodes.
* An edge can be **directed** or **undirected**. 
* A **path** is a sequence of nodes connected by edges.
* A **cycle** is a path that starts and ends at the same node.
* We use an **adjacency list** or an **adjacency matrix** to store a graph.
* **邻接链表 Adjacency list**: `adj_list[i]` is a list of nodes that are connected to node `i`.
  * Advantage: saves space.
  * Disadvantage: takes O(E) time to check if there is an edge between two nodes.
* **邻接矩阵 Adjacency matrix**: `matrix[i][j]` is `True` if there is an edge from node `i` to node `j`, or if they are connected
  by an edge, in case of undirected graph. Otherwise, `matrix[i][j]` is `False`.
     * Advantage: takes O(1) time to check if there is an edge between two nodes.
     * Disadvantage: takes O(V^2) space.

![Storage of graph](https://algorithmtutor.com/images/graph_representation_directed.png)

## Graph Traversal
- Same as traversal of a tree.
- Graphs can have cycles, so we need to keep track of `visited` nodes to avoid infinite loops.
- Difference between backtracking and DFS:
  - The key of **backtracking** is that we don't care about the **node**, we care about the **edge**.

## Table of Questions
- [277. Find the Celebrity](#277-find-the-celebrity-medium) 🍊
- [Union Find](#union-find)

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

#### 💡 Best Solution: O(N) time, O(1) space
Use a integer `c` to keep track of the index of the celebrity. Initially, set `c = 0`.
Iterate through the rest of the people. If `c` knows `i` or `i` does not know `c`, then `c` is not the celebrity, but 
`i` could be the celebrity, so set `c = i`. Otherwise, `c` is still the celebrity.
Eventually, when we jump out of this loop, `c` will be the index of the last possible candidate! We just need to check
if `c` is the celebrity by checking if `c` knows no one else and if everyone else knows `c`.

Time complexity: O(2N) = O(N), using two for loops. Space complexity: O(1).

## Union Find
1. 自反性：对于任何节点 `p`，`p` 和 `p` 是连通的。
2. 对称性：如果 `p` 和 `q` 是连通的，那么 `q` 和 `p` 也是连通的。
3. 传递性：如果 `p` 和 `q` 是连通的，`q` 和 `r` 是连通的，那么 `p` 和 `r` 也是连通的。

How to implement union find?
1. `union(x, y)`: 将 `x` 和 `y` 连通, O(N)
2. `find(x)`: 返回 `x` 所在的连通分量的代表节点, O(N)
3. `connected(x, y)`: 判断 `x` 和 `y` 是否连通, O(N)

How to improve the time complexity?
1. 用`parent`数组记录每一个node的parent node
2. 用`size`记录每一个cluster的size，这样可以让更小的cluster的root node指向更大的cluster的root node，这样可以减少树的高度，
   从而减少 `find(x)` 的时间复杂度。
3. Path compression: 在 `find(x)` 的时候，将 `x` 所在的连通分量的所有节点的 `parent` 都设为这个cluster的root node，这样的话，
   从这些nodes中任意一个node到达root node的路径都是只有一条edge。可以将 `find(x)` 的时间复杂度降低到 O(logN)。

可以把每个cluster里的nodes想像成用一个tree来存储。这个tree是一个多叉树，每个node都有一个parent node，除了root node。这个tree
是自下而上的，也就是每一个node都指向它的parent node，root则指向它自己。

可以通过array来储存这种关系，假设一共有n个nodes，我们可以有一个长度为n的array，`parent`，其中`parent[i]`表示node`i`的parent node的index。
如果`arr[i] == i`，则说明node`i`是root node。
```shell
index  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
par = [1, 1, 1, 8, 3, 0, 5, 1, 8, 8]

# node 9的 parent是node 8
# node 8的 parent是node 8，所以node 8是root node

# node 5的 parent是node 0
# node 0的 parent是node 1
# node 1的 parent是node 1，所以node 1是root node
```

当我们call `union(x, y)`时，我们可以让更小的cluster（tree height更小）的root node指向更大的cluster的root node。

![quick find](https://algs4.cs.princeton.edu/15uf/images/quick-union-overview.png)

### 323. [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Medium)


