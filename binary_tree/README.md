# Binary Tree Problems

**Table of Contents**
- (104) Maximum Depth of Binary Tree (E)
- (543) Diameter of Binary Tree (E)
- (515) Find Largest Value in Each Tree Row (M)

### 104. Maximum Depth of Binary Tree (Easy)

**My solution 1**: Divide and Conquer with Recursive Helper Function

Whether it's possible to define a _recursive function_ that 
calculates the answer of current problem based on the 
solution to the subproblem (subtree)? Yes!

At each node, what needs to be done? At each node, we want to know _max depth of current subtree_, which is the maximum between depth
of current node's left subtree and right subtree plus 1. If node is `None`, the max depth of current subtree whose root is current node is 0.

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

Note: it's easy to notice that the order is **post-order**, why? This is because to know the max depth of current subtree, you need
to know the depth of left subtree and right subtree first to find the max of the two. This is why the root node of a subtree is always visited last.

**My solution 2:** Pre-order traversal of tree
- Use a **global variable** `res` to keep track of maximum depth we have seen so far
- Update `res` if `depth` of current node is greater than `res`
- Default value of `res` is 0, applies to situations where input tree is `None`
- Return type of `traverse()` is `None`
- At each node, calculates depth of current node by adding 1 to depth of parent node, which is passed along as we call the helpder function `traverse()`
- Why pre-order? As we get to a node from its parent node, the depth needs to be updated. After the update, the depth is actual depth of current node, which will be passed to its child nodes

**Summary**:
Pre-order operations only have access to information passed from **parent** nodes, however, post-order operations have access to
information passed up by its **children** (subtrees).

### 543. Diameter of Binary Tree (Easy)
[Tree example](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

This problem is similar to the previous problem. The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
The longest path between any two nodes is actually the sum of max depth of left subtree and max depth of right subtree.

**My solution 1**: Divide and Conquer with Recursive Helper Function

Use a recursive helper method that finds the max depth of a node (the subtree for which the root is current node)
by comparing the depth of its left and right subtrees. Use **post-order** operation to add the max depth
of left and right subtree and compare with global variable `res` to update `res`.

Note: 
- The operation to calculate sum of max depth of two subtrees must be done at **post-order** position, because only
in this way, we can have access to information passed up by its children (subtrees).
- It's important to plan ahead what should be returned by the helper function. The returned value should be a property of the subtree that helps solve the problem.


Time complexity: O(N)

### 515. Find Largest Value in Each Tree Row
Use level-order traversal of binary tree (BFS). Use a queue to store nodes to visit. At the end of every level, 
enqueue a `None` node to indicate that end of level has been reached. Whenever a `None` node is seen, 
increment `level` by one, and add another `None` node to queue (this is because if we have finished processed one level, 
all nodes of next level have been enqueued already). The initial value of `level` is 0 because we will use this as an index for `res` array.
`res` is an array of size _h_ where _h_ is number of levels in tree, at each index `i`, the value is the largest value
in _i_-th tree row. Exit out of the while loop when we have popped a null node and then the length of queue becomes 0.

Time complexity: O(N)


Date: Aug 29, 2023
### 226. Invert Binary Tree (Easy)

**My solution 1: Traversal**

Visit every node in binary tree.

At each node, what needs to be done by recursive function `traverse()`?
- Swap left and right child
- Call `traverse()` on left and right child
- Return nothing (since we are directly modifying tree structure)

What about mapping of nodes? For example, if we have a tree:
```bash
     4
    / \
   2   7
  / \ / \
 1  3 6  9
```
How do we make sure nodes 1 and 9 gets swapped, 3 and 6 get swapped, and not 1 and 3, 6 and 9?

Note that when 1, 3, 6, 9's parent nodes are swapped, their locations
in binary tree change as well.
```bash
# After swapping nodes 2 and 7
     4
    / \
   7   2
  / \ / \
 6  9 1  3
 
# Swap nodes in level 3
     4
    / \
   7   2
  / \ / \
 9  6 3  1
```
Every swap between left and right children of a node results in lower-level subtrees being swapped as well. At this point, keep swapping
the left and right children of a node in lower levels.

**My solution 2: Divide and Conquer**
At every node, what needs to be done?
- Invert left and right subtrees (not swap!)
- Swap left and right subtrees
- Return current node

```bash
# 1. Invert left subtree (root 2)
# 1.1 Go to subtree 1 with children None and None
# 1.2 Go to subtree  3 with children None and None
# 1.3 At node 2, swap left and right subtree
# 1.4 Return inverted subtree root node 2
      4
    /   \
   2     7
  / \   / \
 1<->3  6  9   # (before swap)
 
# 2. Invert right subtree (root 7)
# 2.1 Invert left subtree 6 (children None and None)
# 2.2 Invert right subtree 9 (children None and None)
# 2.3 Swap left subtree 6 and right subtree 9
# 2.4 Return inverted subtree root node 7
      4
    /   \
   2     7
  / \   / \
 3   1 6<->9  # (before swap)
 
# 3. Swap left subtree 7 and right subtree 2
      4
    /   \
   7     2
  / \   / \
 9   6  3  1
```
