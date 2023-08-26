# Binary Tree Problems

### 104. Maximum Depth of Binary Tree (Easy)

**Rationale**: 

Whether it's possible to define a _recursive function_ that 
calculates the answer of current problem based on the 
solution to the subproblem (subtree)? Yes!

At each node, what needs to be done? At each node, we want to know _height of node_. Different from how height is defined 
for binary trees, in this case, the height is the number of layers
of the current subtree (where current node is root). If node is `None`, its height is 0.
This can also be thought of as the _max depth of left and right subtrees_.

**My solution**:
The following helper function aims at finding the max depth of a node's left and right subtrees.
```python3
def dfs(node) -> int:
    if not node:
        return 0
    return max(dfs(node.left)+1, dfs(node.right)+1)
```

At node 15, left and right subtrees are both `None`, with height = 0. Node 9 adds height of 1 to subtree, so max depth at node 9 is max(0+1, 0+1) = 1.
Same applies to node 7. At node 20, max depth is max(1+1, 1+1) = 2. The rest of it is just the same thing.
```angular2html
Node:  9 	Max depth at node:  1
Node:  15 	Max depth at node:  1
Node:  7 	Max depth at node:  1
Node:  20 	Max depth at node:  2
Node:  3 	Max depth at node:  3
```

Note: the order in which nodes are visited is _post-order_, left subtree visited first, then right subtree, then root node.
