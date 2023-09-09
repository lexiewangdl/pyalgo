# Binary Tree Problems

**Table of Contents**
- 104 - Maximum Depth of Binary Tree 🍏
- 543 - Diameter of Binary Tree 🍏
- 515 - Find Largest Value in Each Tree Row 🍊
- 226 - Invert Binary Tree 🍏
- 116 - Populating Next Right Pointers in Each Node 🍊
- 114 - Flatten Binary Tree to Linked List 🍊
- 124 - Binary Tree Maximum Path Sum 🍎
- 654 - Maximum Binary Tree 🍊
- 105 - Construct Binary Tree from Preorder and Inorder Traversal 🍊
- 106 - Construct Binary Tree from Inorder and Postorder Traversal 🍊
- 889 - 🚩 Construct Binary Tree from Preorder and Postorder Traversal 🍊
- 652 - 🚩 Find Duplicate Subtrees 🍊 
- 297 - Serialize and Deserialize Binary Tree 🍎
- 538 - Convert BST to Greater Tree 🍊
- 98 - Validate Binary Search Tree 🍊
- 96 - 🚩 Unique Binary Search Trees 🍊 
- 95 - Unique Binary Search Trees II 🍊
- 700 - Search in a Binary Search Tree 🍏
- 701 - 🚩 Insert into a Binary Search Tree 🍊 
- 450 - 🚩 Delete Node in a Binary Search Tree 🍊 
- 257 - Binary Tree Paths 🍏
- 129 - Sum Root to Leaf Numbers 🍊 
- 199 - Binary Tree Right Side View 🍊 
- 1022 - Sum of Root To Leaf Binary Numbers 🍏

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

### 116. Populating Next Right Pointers in Each Node (Medium)
**My solution 1: Classic BFS Traversal**

Use queue to store next nodes to visit, traverse with BFS.
Use `None` to indicate level change. Add `None` node to queue after done processing with each level.
Whenever a `None` node is dequeued, it means that nodes in this level have been processed, and nodes in next level
have been enqueued. At this point, add another `None` node, which will be level change indicator for next level.
If two `None` nodes are dequeued in a row, reached end of tree, break out of while loop.

- Initialize queue for BFS
- Add root node and level change indicator (None) to queue
- While there are still nodes to visit:
  - Current node to process is the node we pop from queue
  - Check if current node is `None` (level change indicator):
    - (1) check if queue is empty now
    - (2) check if next node to visit is also `None`
    - If either one of the conditions above is met, reached end of tree, return
    - Otherwise, add another level change indicator `None` to queue
  - If current node is not `None`, process:
    - (1) Make current node's `next` pointer point to next node to visit (if current node is last node in this level, the next node to visit will be `None`)
    - (2) Enqueue left and right children of current node (only if child is not None), don't enqueue any None nodes because it will break the level change rules

Note: input tree is **perfectly binary tree**, in simple terms, this means that all leaf nodes are at the maximum depth of the tree, and the tree is completely filled with no gaps.

Time complexity: O(n) where n is number of nodes in tree
Space complexity: O(w) where w is maximum width of binary tree, in terms of **perfect binary tree**, w is number of leaf nodes

**My solution 2: Traversal**

Naive thinking: just connect a node's left child to its right child

Problem: this only connects left and right children of the SAME node. However, we also need to connect adjacent nodes that don't have the same parent
```bash
# Before
  A     B
 / \   / \
C  D   E  F

# After
  A    ->   B
 / \       / \
C ->D (?) E ->F
```

Solution: define a helper function `traverse()` that takes two adjacent nodes from the parent level as input, and the 
helper function does the following for every pair of input nodes ...
- (1) Check if left and right parent are null (tree is perfect binary tree, so either both nodes are not null, or both nodes are null)
- (2) Connect left parent to right parent, `left_parent.next = right_parent`
- (3) Process the parent nodes' children...
  - (a) For left parent, connect left child to right child
  - (b) Connect right child of left parent to left child of right parent
  - (c) For right parent, connect left child to right child

Note: it's somehow like a tertiary tree, where AB is the parent node,
 CD is left child, DE is middle child, and EF is right child

### 114. Flatten Binary Tree to Linked List (Medium)

**My solution:**

Tree Example
```bash
     1
    / \
   2   5
  / \   \
 3   4   6
```

**Attempt: Traversal**

Since the problem is asking for a linked list in which the nodes
are in order of pre-order traversal, it's natural to think about
traversing the tree in pre-order and then adding each node to correct position in linked list.
However, this solution is not possible.

For example, with pre-order DFS, when we are processing node 2, we might want to set it to 1.right. 
However, the node 5 is already at 1.right, what should we do with this node? Also, even if we set 1.right to 2 and 2.right to 5, where
should nodes 4 (originally 2.right) go?

Anyways, this is not the correct thinking to approach this problem.

```bash
     1
    / \
       2
      / \
 4?  3   5
          \
           6
```

**Solution: Divide and Conquer**

With the _top-down approach_, we will have problems dealing with 
existing nodes at places where we want to place current node.

An alternative way to think about this question is, dividing the tree into _subproblems (subtrees)_. For each
subtree, do something to flatten the subtree. For example, for the subtree with root node 2, we can do the following:
```bash
   2         2       2
  / \  -->  /   -->   \
 3   4     3           3
            \           \
             4           4
```
This way, by processing nodes _bottom-up_, we can make sure that every subtree we are dealing with is already flattened,
and we just need to make sure the left subtree and right subtree are correctly concatenated into one linked list.

Note: Return type of `flatten()` is null, we need to use O(1) extra space, modifying the tree in-place

**When to do the processing?**

To adopt a _bottom-up_ approach, we must use _post-order_ processing. We need to get to leaf nodes first, and then, while
we are travelling back from leaf nodes to root nodes, we flatten the subtrees.

**What needs to be done at each node (for each subtree)?**
- **Base case**: check if `node` is null (if `node` is null, return)
- Recurse on `node.left` and `node.right` (remember we are doing _post-order_ processing)
- Check if `node.left` is null, if so, don't need to do anything
- If `node.left` is not null:
  - (1) append right subtree to left subtree
    - Here, another thing to keep in mind is we can't just do `node.left.right = node.right`, because `node.left` can be a chain of nodes
    - Must navigate to the last node in `node.left` chain, and then set the last node's right pointer to `node.right`
    - Use a `while` loop to navigate to last node in `node.left` chain/subtree
  - (2) Make left subtree the right subtree: `node.right = node.left`
  - (3) Set left subtree to be null: `node.left = None`

Visualize the process:
```bash
# The processing for left subtree is illustrated above
# Assume that step has been done
     1            1            1        1
    / \          / \          /          \
   2   5   -->  2   5   -->  2     -->    2
  / \   \        \   \        \            \
 3   4   6        3   6        3            3
                   \            \            \
                    4            4            4
                                  \            \
                                   5            5
                                    \            \
                                     6            6
```

### 124. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (H)

**My solution: Divide and Conquer**

**What needs to be done at each node?** 
We want the helper function to return the maximum single-sided path sum that goes through the current node.
This can be the maximum of the following:
- `node.val + findMax(node.left)`: the maximum path is the maximum path of left subtree plus the current node
- `node.val + findMax(node.right)`: the maximum path is the maximum path of right subtree plus current node
- `node.val`: in case where current node's val is greater than previous two options, for example:
  ```python
  # node.val = 2
      2
     / \
   -5  -6
  # left subtree max path = -5
  # right subtree max path = -6
  ```
Thus, at each node, this helper function returns the maximum path sum at one side of the tree (not the sum of left and right sides).
This is because this value will be passed up (when we do post-order processing) and then used to find the total path sum (which
will be the left_max_path_sum + right_max_path_sum + node's value).
The returned value would be `max_single_path = max(node.val, left_sum + node.val, right_sum + node.val)`.


Post-order processing:
- Use a global variable `ans` to keep track of maximum total path sum we have seen
- Update this variable if current max path sum is greater: `self.ans = path_sum if path_sum > self.ans else self.ans`
- Max path sum at current node is `path_sum = max(max_single_path, left_sum + right_sum + node.val)`


## Construct Binary Tree Problems
Problems related to constructing binary trees are usually solved using the divide and conquer method.

To construct a binary tree, construct the root node first, then recursively construct left subtree and right subtree.

### 654. Maximum Binary Tree (M)
**My solution 1: Divide and Conquer**

**Function `constructMaximumBinaryTree()`:**
- Parameters: integer array `nums`, input array with node values from which we construct the tree
- Return type: tree node

**At each node (for each subtree), what needs to be done?**
- Check if `nums` is empty, if yes, return null
- Find the maximum element in `nums`, use this value to construct the root node
- The slice to the left of the max element in `nums` is used to construct left subtree, pass to recursive call of function as parameter
- The slice to the right of the max element in `nums` is used to construct right subtree

Note: make sure that slicing is correctly done. Left sub-array should be `nums[:max_idx]` and right sub-array 
should be `nums[max_idx+1:]`. If the already found max value is included in left or right subarray,
will lead to `RecursionError: maximum recursion depth exceeded`.

**Problem with this solution:** space complexity! A lot of wasted space as we pass in copies of left and right sub-arrays
as params to recursive function calls. No need to store these copies of subarrays.

**My solution 2: Optimize space complexity with left and right pointers**

This method will require a helper method that needs to be defined as the following...
- Parameters: integer array `nums`, int `left`, int `right` (where left and right are indices of sub-array boundaries)
- Return type: tree node

The idea is the same, at _pre-order_ position, construct root node.
When recursively calling helper function, modify the boundaries `left` and `right`.

```python
  # Pseudocode
  def construct(nums: list, left: int, right: int) -> TreeNode:
    # pre-order position:
    # find the index of max element in nums[left:right]
    node_idx = ... 
    # if no max value, return None
    if node_idx == -1:
      return None
    # build root node based on max value
    node = TreeNode(max_val)
    
    # recursive calls
    node.left = construct(nums, left, node_idx)
    node.right = construct(nums, node_idx + 1, right)

    return node
```

## 105. Construct Binary Tree from Preorder and Inorder Traversal
**My solution:**
Similar to previous problem, to construct a binary tree, we need to...
- Build root node
- Build left subtree (recursively)
- Build right subtree (recursively)

We also need to keep in mind certain properties of pre-order and in-order traversal.
- **Preorder:** [ROOT, LEFT_SUBTREE, RIGHT_SUBTREE]
- **Inorder:** [LEFT_SUBTREE, ROOT, RIGHT_SUBTREE]

From this, we know that, given a pre-order array, the first element is our **overall root** node.
The same allies to preorder sub-arrays of subtrees.
We also know that, with in-order array, all elements in left subtree are to the left of root, and all
elements in right subtree are to the right of node.
By accessing the first element in preorder array, we can find the root node; then, by searching for the
index of this element in inorder array, we can find the slices for left and right subtrees.

How to keep track of left and right boundaries of left and right subtrees in inorder array? 
- Based on experience from previous problem, we don't want to pass copies of array slices as params
- Use `left` and `right` pointers to keep track of boundaries

How to keep track of the index of current node we are building in preorder array?
- We are doing pre-order processing
- The order by which we build the nodes is same as order of elements in preorder array
- Use a global variable `self.preorder_idx` to keep track of index of current node in preorder array
- Update this everytime we have finished building the node (before recursive calls)

However, this approach has one problem. Everytime we build a node, we need to loop through half of the in-order array 
(or subarray) to find the index of curr node in inorder array.
The problem states that all nodes have different values.
Thus, we can use a dictionary (or hash map in Java) to store the mapping between each node's value and their corresponding
index in inorder array. Store this as a global variable: `self.inorder_map = dict()`.
This way, the runtime is significantly reduced.

### 106. [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/) (Medium)

Similar to previous problem, need to understand post-order and in-order arrays:
- Post-order: [LEFT_SUBTREE, RIGHT_SUBTREE, ROOT]
- In-order: [LEFT_SUBTREE, ROOT, RIGHT_SUBTREE]

![Post-order and in-order](https://labuladong.gitee.io/algo/images/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%B3%BB%E5%88%972/6.jpeg)

Different from previous problem, this time, we can't just use one integer to keep track of our position in post-order array.
We can do this we pre-order array because our order of processing is pre-order processing.
With post-order array, we need to use two pointers to keep track of boundary of subtree's subarray.

We have four pointers in total:
- `il`: starting point (left boundary) of inorder subarray
- `ir`: ending point of inorder subarray (non-inclusive)
- `pl`: starting point of preorder subarray
- `pr`: ending point of preorder subarray (non-inclusive)

The process to determine `il` and `ir` is same as in previous problem.

Our helper function can be defined as followed:
```python
def build(inorder: list, preorder:list, 
          il: int, ir: int,
          pl: int, pr: int) -> TreeNode:
    ...
```

**How to determine the left and right boundaries for post-order subarrays?**
- For left subtree's post-order array:
  - Starting point is `pl`, same as passed in param
  - Ending point is `pl + LENGTH_OF_LEFT_SUBARRAY`
  - How to find length of left subarray?
    - The length of left subarray is `node_idx_inorder - il`
  - So, for left subtree, the new boundary should be: `pl, pl+(node_idx_inorder-il)`
- For right subtree:
  - Ending point is `pr-1`, since the last element is root and we need to exclude it from subarray
  - Starting point is the ending point of left subtree: `pl, pl+(node_idx_inorder-il)`

The rest is just same as previous problem. Note: remember to build a dictionary to store mappings
of node values to their inorder indices.

### 889. [Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/) (Medium)

Given preorder and postorder traversal results:
- Preorder: ROOT, LEFT_SUBTREE, RIGHT_SUBTREE
- Postorder: LEFT_SUBTREE, RIGHT_SUBTREE, ROOT

What needs to be done at every step?
1. Construct current node
   2. The value of current node is the first element in preorder range, which is same as last element in postorder range
3. Recursively build left and right subtrees
   4. How to find the boundary indices of left and right subtrees?

How to find the boundaries for left and right subtrees?
- For left subtree...
- (1) The root node of left subtree is right next to current node in preorder array, this is the pre_order left boundary for left subtree (`pre_left + 1`)
- (2) Find the index of root of left subtree in post order array, using a dictionary that maps elements to their indices in postorder array.
- (3) The length of left subtree can be found by `left_subtree_root_idx_post - post_left + 1`
- (4) Thus, the left and right _preorder_ boundaries are:
  - Left: `pre_left + 1`
  - Right: `pre_left + 1 + length_left_subtree`
- (5) The left and right _postorder_ boundaries:
  - Left: `post_left`
  - Right: `post_left + length_left_subtree`
- For right subtree...
- (1) _Preorder_ boundaries:
  - Left: `pre_left + 1 + length_left_subtree` (same as preorder right boundary of left subtree)
  - Right: `pre_right`
- (2) _Postorder_ boundaries:
  - Left: `post_left + length_left_subtree`
  - Right: `post_right - 1` (which is index of current node)

```bash
# preorder                        # postorder
curr node                     post_left = 0        curr node
 |                                 |                 |
[1, 2, 4, 5, 3, 6, 7]             [4, 5, 2, 6, 7, 3, 1]
    ^                                    ^
    |                                    |
  root of left subtree, idx = 1        root of left subtree, idx = 2
  
  length_left_subtree = idx_root_left_subtree_post - post_left + 1 = 2 - 0 + 1 = 3
 
```

Note: to handle IndexOutOfRangeError when accessing root node of left subtree (`preorder[pre_left+1]`), add a conditional statement:
return `Node` (current node) if `pre_left + 1 == pre_right`.


### 652. [Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/description/) (Medium)

**1. Given a subtree, what needs to be done?** 

Given a subtree, we want to come up with a way to **represent current subtree**. 

This is because to figure out whether current subtree is a duplicate or not, we must be
able to have a pool of representations for all subtrees. We can use a set to store unique subtrees we've seen,
or use a map to store unique subtrees and the number of times we have seen each unique subtree.
This representation
needs to be _hashable_, because we want to store it in a set or map.


**2. Where/when to do this processing?**

One thing special about _post-order processing_ is that we have access to information passed
up from child nodes/subtrees. With _post-order processing_, we travel each of the child nodes first, return a value for each,
based on returned values, we can construct a representation for current subtree.

If we use _pre-order_ or _in-order_ processing, when we are processing a node, we don't know the structure
of the current subtree (because we haven't traveled all child nodes yet).

**3. How to represent a subtree?**

A very intuitive way is to use strings. Since we are doing post-order processing, the order of node values
in string representation of subtree would be same as post-order traversal.

For example, the string representation of the following tree would be "132".
```bash
   2
  / \
 1   3
```

However, there are several problems with this naive string representation. Given the following trees:
```bash
    0         0
   / \       / \
  0  null  null 0 
# before:
# "00"      "00"
# after:
# "0 0"     " 00"
```
The string representation for both trees would be "00", because we don't effectively take care of null nodes.
Thus, we can use whitespace to represent null nodes.
(I've also seen other people use # instead of whitespace).

Another problem comes with edge cases like this:
```bash
   2          22
  / \        / \
 1   12     1   1
# before:
# "1122"     "1122"
# after:
# "1,12,2"   "1,1,22"
```
For subtrees with special values like this, the string representation for both trees is the same, despite the fact that
the subtrees have different values at different positions. Thus, we need to differentiate each node from another, using "," as
a separator.

**4. Recursive construction of string representations**

We have decided to make helper function `represent_subtree()` return a string that represents current subtree.
How to use it recursively to build string representation for entire tree?
```python
curr_subtree = self.represent_subtree(node.left) + "," + self.represent_subtree(node.right) + "," + str(node.val) + ","
```
Embed recursive calls on left and right subtrees in one line. Concat returned vals properly.

**5. Check if subtree is a duplicate**

My initial thought was to use a set to store string representations of subtrees.
However, the problem requires that each duplicate must only be returned once. If I use a set, I would either
return duplicates multiple times (if there are more than 2 duplicates) or need to use another
data structure to store seen duplicates.

Thus, it's best to use a `dict` or `Counter` to store the number of times we have seen this duplicate. If we have seen 
the same tree structure twice, add current node to `result` (list of TreeNodes).

### 297. [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/?envType=daily-question&envId=2023-09-01) (Hard)
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

In terms of this problem...
- **Serialization**: come up with a string representation of binary tree
- **Deserialization**: construct binary tree from serialized data

In what ways can we serialize a tree so that its output can be deserialized to construct the exact same tree?
- Store only _one_ traversal result (either pre, in, or post order):
  - If we don't represent _null nodes_ with `#` (or whitespace in previous problem), then **we cannot restore the exact same binary tree given _one_ traversal result**.
  - If we do represent _null nodes_ with `#`, **can restore the exact same binary tree with _preorder_ traversal or _postorder_ traversal results**, but not inorder traversal results. This is because we can't figure out which node is the root node if we only have in-order results.
- Store multiple traversal results:
  - Given a combination of _preorder + inorder_ or _inorder + postorder_, we will be able to restore the exact same binary tree (see problems 105 and 106)
  - If we are given the combination _pre-order + post-order_, then there can be multiple solutions, and we can't restore the exact same binary tree (see problem 889).

Since storing multiple traversal results requires higher space complexity, I didn't write solutions that way.
My two solutions: (1) store preorder representation with null pointers, (2) store postorder representation with null pointers,
and deserialize based on my representations.

#### Pre-order Solution
- Serialize results, `#` indicates null node, `,` separates nodes
  - Note: serialized result should be `"ROOT,[LEFT_SUBTREE],[RIGHT_SUBTREE]"`, there should be no trailing `,`s, otherwise, when we split result by `,`, there will be empty strings which cause troubles
- Before deserialization, split serialized result by `,`, store this list as global variable
- Use a global variable `deserialize_idx` to keep track of index of current node's value
  - Initialize to 0
- Decrement `deserialize_idx` after constructing current node (before recursive calls)

#### Post-order Solution
Everything is the same as pre-order solution, except...

With post-order serialization, the serialized result looks like `[LEFT_SUBTREE],[RIGHT_SUBTREE],ROOT`.
We know that root node's value is the final element in list, and root node of right subtree is to the immediate left of overall root.
However, we can't easily find out where the root of left subtree is.

```bash
# post order
     1
    / \
   2   3
      / \
     4   5
     
# serialized: "#,#,2,#,#,4,#,#,5,3"
```

Thus, the key is, when constructing binary tree based on serialized result,
construct right subtree first, and then construct left subtree.

- Serialize results in _post-order_, `#` indicates null node, `,` separates nodes
  - Note: serialized result should be `"[LEFT_SUBTREE],[RIGHT_SUBTREE],ROOT"`, there should be no trailing `,`s
- Before deserialization, split serialized result by `,`, store this list as global variable
- Use a global variable `deserialize_idx` to keep track of index of current node's value
  - Initialize to length - 1
- Decrement `deserialize_idx` after constructing current node (before recursive calls)
- Recursively **build right subtree first**, then build left subtree

## Binary Search Tree (BST) Problems

### 230. k-th Smallest Element in a BST
In-order traversal result of a BST goes in ascending order.
To find the k-th smallest element, just do in-order traversal and return the k-th element.

**My solution:** Use two global variables, `val` to keep track of value of k-th smallest element, and `n` to keep track
of number of nodes we have visited. Do in-order processing: check whether n is equal to k, if so, return, increment n
at every step.

## Summary
1. **Construct binary tree problems**:
divide and conquer
Construct tree = construct root node + construct left subtree + construct right subtree

2. **Post-order processing**:
post-order processing enables us to have access to information passed up from subtrees/child nodes. This can be a value
or something else (depends on return type of recursive helper function). **If the question is about subtrees, it's very
likely that we need to do post-order processing.**

### 538. Convert BST to Greater Tree (Medium)
**My solution: Traversal**

By traversing through every single node in descending order (process nodes with greater
values first), and keeping track of the sum of processed nodes' values, convert binary search tree
to a greater tree.

**In-order traversal of binary search tree** gives results in ascending order. To get descending order,
just traverse right subtree first.
```python
traverse(node.right)
# process current node
traverse(node.left)
```

Use a global variable `greater_sum` to keep track of sum of nodes' values that are greater than current node's value
(which is the same as sum of all nodes we have processed).
Update the value of current node at in-order position, `node.val = self.greater_sum = node.val + self.greater_sum`.

### 98. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/) (Medium)
**My solution 1: in-order traversal**

Traver the tree once. Use a global variable to keep track of maximum
value we have seen (to the left of current node).
If current node's value is equal to or less than maximum value we have seen,
then tree is not a valid BST.
See simple pseudocode below:
```python
seen_max = -math.inf
ans = True

def traverse(node):
    traverse(node.left)
    if node.val <= seen_max:
        ans = False
    seen_max = node.val  # update max val seen to the left of curr node
    traverse(node.right)
```

Space complexity is O(1), simply store two variables. However, we can use less extra space.

**My solution 2: min and max**

Function parameters:
- `r_min`: minimum value seen in right subtree
- `l_max`: minimum value seen in left subtree

Return type: boolean
- Return true when current node is null
- Or when both current node's left subtree and right subtree are BSTs, and current node is less than `r_min` and greater than `l_max`

  For example: `return self.isValidBST(root.left, l_max, root.val) and self.isValidBST(root.right, root.val, r_min)`

### 96. [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/description/) (Medium)
Given an integer `n`, how to find the number of unique binary search trees with `n` nodes from `1` to `n`?

**Divide and conquer:** Given a root node, the number of unique binary search trees is equal to
number of unique BSTs for left subtree times number of unique BSTs for right subtree.

For example, given the val `n=5`, and root node is `3`:
```bash
   3
  / \
 L   R
# num_unique_bsts = 2 * 2 = 4
 
# Left subtree possibilities, num_unique_bsts_left = 2
1         2
 \       /
  2     1

# Right subtree possibilities, num_unique_bsts_right = 2
4       5
 \     /
  5   4
```

Thus, we want our recursive helper function to return **number of unique BSTs**. Then, we can recursively
call this function until we reach a base case.

**What is the base case?**
- If there are no nodes in left subtree, we get a `null` tree, which is 1 unique case
- If there is only 1 node, we get a one-node tree, which is 1 unique case

**How to reach the base case?**
- Define two integers `left` and `right`, which corresponds to the smallest node val and largest node val, and we use all integers within this range (inclusive) to build the tree
- Each node can be the root node, so we **use a for loop within this range**, and recursively call this function by modifying `left` and `right` values

**Code skeleton**
```python
def helper(left, right):
    if left >= right:
        return 1
    
    num_bsts = 0
    
    for i in range (left, right + 1):  # inclusive
        num_bsts_left = helper(left, i-1)
        num_bsts_right = helper(i+1, right)

        num_bsts = num_bsts_left * num_bsts_right

    return num_bsts
```

However, this method is quite **inefficient** because we need to repeatedly calculate the same subproblem many times, sort of like Fibonacci number.
This is where we can use **dynamic programming**, using a **memo** to store results of subproblems.

This memo is a 2D-array of size _n*n_.
Note that when initializing the array, we must do `[[0 for col in range(n)] for row in range(n)]` instead of `[[0] * n] * n]`,
because the latter will create `n` copies of the same array! In this case, every time we modify one element in one row,
all other rows mirror the same changes.

### 95. Unique Binary Search Trees II (Medium)
The key to constructing binary trees is: build root node first, then recursively build left and right subtrees.

**Helper function parameters:**
- Similar to previous problem, use two integers `left` and `right` to indicate the left and right boundaries (inclusive) of node values
- Return type should be a list of tree nodes, which contains all possible tree structures, given that all node values are within range `left` and `right` (inclusive)

**Base case:**
- If `left > right`, subtree should be a null tree, return `[None]`
- If `left == right`, subtree can only be one single node, return `[TreeNode(left)]`
- Else, we need to recursively call our function to find possible left subtrees and right subtrees.
  ```python
  def build(left, right):
      ... # define base cases
  
      result = []
  
      for i in range(left, right+1):
          left_trees = build(left, i-1)
          right_trees = build(i+1, right)
  
          # 2 embedded for loops
          for left_tree in left_trees:
              for right_tree in right_trees:
                  root = TreeNode(i)  # create new subtree root node
                  root.left = left_tree
                  root.right = right_tree
                  result.append(root)
  
      return result
  ```
  
Similarly, we can also use a data structure to store computed results, so that we don't have to compute the same subproblem multiple times.
Here, I used a dictionary.

## BST: Binary Search
Very helpful code structure to solve binary search problems.
```python
def search(node, target):
    if node.val == target:
        # do something
    if node.val < target:
        search(node.left, target)
    if node.val > target:
        search(node.right, target)
```

### 700. [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/) (Easy)
Function parameters:
- `root`: current node to check
- `val`: target value

Return:
- Return `root` if current node's value is equal to `val`
- Return `None` if current node is null
- Check left and right subtrees, return result of recursive call, e.g. `return self.searchBST(root.left, val)`
  - If left subtree contains a node whose value equals `val`, then returned value will be that node
  - Same applies to right subtree

Only check left subtree if current node's value is greater than `val`, which means that a node
with value less than current node's value can only be in the left subtree. Vice versa for right subtree.

### 701. [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/description/) (Medium)

Find where to insert new node first, then do insertion.

Problems that involve **modifying the structure of BST** usually require the function to **return a tree node**,
and we need to utilize the returned node.

**Where to insert new node?**
- According to BST invariants, the root node of a BST must be greater than all values in the left subtree
- and also less than all values in the right subtree
- Thus, we can find the correct position where new node needs to be inserted, by
- travel to the right subtree if `val` is greater than current root's value
- or go to the left subtree if `val` is less than the current root's value
- when we find an **empty spot**, we can add new node there

**Function parameters:**
- `root`: current node to process
- `val`: value of node to insert

**Return type:**

Return type is `TreeNode()`. At each step, we insert the node when two conditions are satisfied:
- (1) the position where we want to insert new node satisfies BST invariants (i.e. if it is the left child of a root node of a subtree, `val` should be smaller than root val)
- (2) this position is not occupied, i.e. `null`

The first condition is done by if conditional statements, `if root.val < val`, call function on right child, and
if `root.val > val`, call function on left child.
The second condition is checked by `if not root: return TreeNode(val)`.
This returned newly created node is then passed up to earlier function calls of root nodes.
This is why we need to set the corresponding child to be the new node:
```python
if root.val < val:
    root.right = self.insertIntoBST(root.right, val)
if root.val > val:
    root.left = self.insertIntoBST(root.left, val)
```
Otherwise, `root` will be returned. This is because if the left child or right child position is occupied, we 
are not going to create a new node, instead, we will keep the original node. Thus, the final line is `return root`.


### 450. [Delete Node in a Binary Search Tree](https://leetcode.com/problems/delete-node-in-a-bst/description/) (Medium)
 
This is also a problem that requires modifying the structure of the tree, the return type of the function should be `TreeNode`.

- Find the node to delete
- Delete the node

**How to delete a node?**
- If both the node's left child and right child are null, delete directly (return `None`)
- If either there is only one child, set the non-null child as current node (`if not root.left: return root.right`, vice versa)
- If the node has two children:
  - There are two solutions: (1) find the largest node in left subtree and make it this node, or (2) find the smallest node in right subtree and make it this node

**How to find the largest child in left subtree?**

We know that the left subtree is also a BST, thus, the root node of left subtree is greater than
all nodes to its left. We only need to find the right-most bottom-most node of this
subtree, which can be easily done by the following:
```python
while node.right:
    node = node.right
return node
```

**How to set the largest child in left subtree as current node?**
1. Find the largest child in left subtree
2. Delete the largest child in left subtree (this can be done by calling `deleteNode()`, which is the function we're trying to build)
3. Make current node (the node to delete)'s left and right child attach to this new node
4. Return largest child (remember that at every recursive call, we are returning the node we are processing right now)

## Traversal Problems

### 257. [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/) (Easy)

To find all paths to leaf nodes in a binary tree, we need to traverse the tree once.

Use a `path` variable (which is a string), passed down as a parameter of `dfs()` to keep track of path to current node.
When processing, if current node does not have any children (`if not node.left and not node.right`), add path to a 
list `ans` (a global variable). Return this list eventually.

### 129. [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/) (Medium)

Similar to previous problem, use a string to build the numbers that represent each path from root to leaf.
Eventually, convert strings back to integers and add them up.

### 199. [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/) (Medium)

Two solutions:
(1) use BFS, keep track of right-most child in each level,
(2) use DFS, visit right children first, then left children.

**My solution: DFS**

**Pre-order** processing of root node, this is because the resulting list of right side view
needs to be ordered top-down (parent comes before child).

My initial plan was to only traverse the right-most branch, and stop immediately when leaf node is reached. However, this is 
problematic because there can be examples like this:
```python
     3
    / \
   1   2
  /
 0
  \
   5
```
If only visit right-most branch, result will be `[3, 2]`, but the answer should be
`[3, 1, 0, 5]`.

Thus, we need a `dfs()` that keeps track of current level of node. This `level` is also used as
index in the resulting list. We only want one value (the right-most one) at each index.

```python
def dfs(node, level):
    if not node:
        return
    
    # pre-order processing
    ...

    dfs(node.right, level+1)  # visit right child first
    dfs(node.left, level+1)
```

### 1022. [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/) (Easy)

**My solution 1:**
- Traverse binary tree with DFS, store each individual path from root to leaf as a string (e.g. "1011") in a global list
- In the end, for each string (number) in list, convert the binary number to decimal number

**How to convert binary to decimal?**
Starting from the last digit, multiply the number by 2^0, increment the power by 1 every time we move one digit to the left.
For example: `1011 = 1*2^0 + 1*2^1 + 0*2^2 + 1*2^3 = 1 + 2 + 0 + 8 = 11`

**Runtime analysis:**
For the recursive part, we visit every single node in the tree once.

For the calculation part, the runtime is approximately `O(num_leaf_nodes * average_tree_length)`, where number of leaf nodes 
is the number of binary numbers we have, and average tree length is average number of digits in binary numbers.



