# Coding Interview Cheatsheet

## Table of Contents
1. Arrays
2. ..
3. ..
4. ..
5. ..
6. ..
7. ..
8. ..
9. ..
10. [Graphs](#10-graphs)
    - [Graph Representation](#graph-representation)
    - [Cycle Detection](#cycle-detection)
    - [Topological Sort](#topological-sort)
11. ..
12. ..


## 10. Graphs

#### Graph Representation
- Adjacency list: use a dictionary, key is node, value is a list of neighbors, `{0: [1, 2], 1: [3]}`.
- Adjacency matrix: use a 2D list, `[[0, 1, 1], [0, 0, 0], [0, 0, 0]]`. `matrix[i][j]` is 1 if there's an edge between node `i` and `j`.

#### Cycle Detection
- Use `build_graph(num_nodes, edges)` to build the graph from the given edges, store in adjacency list (dict).
- Use `visited` to keep track of checked nodes.
- Use `on_path` to keep track of nodes in the current path, if we encounter a node that's already marked as `True` in `on_path`, then we have a cycle.
- Use `dfs(node)` to traverse the graph.
  - Base case: if `on_path[node]`, we have cycle, return. If `visited[node]`, return, don't check again.
  - Pre-order operation: mark current node as visited and on path.
  - Recursive case: use a `for` loop to traverse the neighbors of the current node.
  - Post-order operation: mark current node as not on path.
- Note that `dfs()` must be called on every single node, since not all nodes are connected.

#### Topological Sort
- Same as above, except that at **post-order position**, append current node to a global variable `post_order_result`.
- Return the postorder_result in reverse order, which is `ans = postorder_result[::-1]`.