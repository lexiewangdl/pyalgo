# Lowest Common Ancestor (LCA)

## Scenarios
- `q`和`p`的LCA不是`q`或`p`本身，而是一个节点`r`，满足`r`是`q`和`p`的祖先节点，且`r`的深度尽可能大。
- `q`和`p`的LCA是`q`或`p`本身。

## Code Template

- 这是最基本的框架，适用于在二叉树中寻找**两个节点**的最近公共祖先节点。
- 但是，节点必须存在于树中，而且不能有重复值，否则需要修改代码。

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # 在二叉树中寻找 val1 和 val2 的最近公共祖先节点
    def find(root, val1, val2):
        if not root:
            return None
        
        # 前序位置
        if root.val == val1 or root.val == val2:
            # 如果遇到目标值，直接返回
            return root
        
        left = find(root.left, val1, val2)
        right = find(root.right, val1, val2)
        
        # 后序位置，已经知道左右子树是否存在目标值
        if left and right:
            # 当前节点是 LCA 节点
            return root
        
        return left if left else right
    
    return find(root, p.val, q.val)

```

## Example

### 1676. [Lowest Common Ancestor of a Binary Tree IV](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/) (Medium)
- 与在二叉树中寻找两个节点不同，这道题要求是在二叉树中寻找**多个节点**的最近公共祖先节点。
- Input `nodes` 是一个列表，里面包含了多个节点。

**Solution**
- 创建一个`values = set()`，用来存储所有的需要寻找的节点值。因为题目中说了节点值不会重复，所以可以用`set`存储`node.val`。
- 然后开始DFS遍历二叉树，在每一个节点上，需要做如下操作：
  - 如果当前节点的值在`values`中，那么直接返回当前节点。
  - 继续在左右子树里进行寻找，将左右子树的返回值分别赋值给`left`和`right`。 
  - 如果`left`和`right`都不为空，那么当前节点就是我们要找的多个节点中的两个节点的LCA，直接返回当前节点`return root`。
  - 如果`left`和`right`只有一个不为空，那么返回不为空的那个节点。

**Example**:
```angular2html
Tree:
      3
     / \
    5   1
   / \ / \
  6  7 2  4

nodes = [6, 7, 2, 4]
```
- 首先在根节点3上，发现3不在`values`中，继续在左右子树上寻找。
- 在节点5上，发现5不在`values`中，继续在左右子树上寻找。
- 在节点6上，发现6在`values`中，返回6。
- 在节点7上，发现7在`values`中，返回7。
- 回到节点5，发现`left`（节点6）和`right`（节点7）都不为空，所以返回5。
- 回到根节点3，继续在右子树上寻找。
- 在节点1上，发现1不在`values`中，继续在左右子树上寻找。
- 在节点2上，发现2在`values`中，返回2。
- 在节点4上，发现4在`values`中，返回4。
- 回到节点1，发现`left`（节点2）和`right`（节点4）都不为空，所以返回1。
- 回到根节点3，发现`left`（节点5）和`right`（节点1）都不为空，所以返回3。
- 所以最终返回的是跟节点3。


