# 226. Invert Binary Tree
from tree_node import TreeNode

# Solution 1: Traversal
def traverse(node) -> None:
    if not node:
        return

    # At every step, swap left and right child of node
    temp = node.left
    node.left = node.right
    node.right = temp

    # Continue doing the same for left and right child
    traverse(node.left)
    traverse(node.right)


def invertTree(root):
    traverse(root)
    return root


# Solution 2: Divide and Conquer
def invertTree(self, root) -> TreeNode:
    if not root:
        return root

    # Invert left and right subtrees
    leftSubtree = self.invertTree(root.left)
    rightSubtree = self.invertTree(root.right)

    # Swap left and right subtrees
    root.right = leftSubtree
    root.left = rightSubtree

    return root
