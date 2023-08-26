# 104. Maximum Depth of Binary Tree
from tree_node import TreeNode


def dfs(node) -> int:
    if not node:
        return 0
    max_depth = max(dfs(node.left)+1, dfs(node.right)+1)
    print("Node: ", node.val, "\tMax depth at node: ", max_depth)
    return max_depth


def maxDepth(root) -> int:
    return dfs(root)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    maxDepth(root)



