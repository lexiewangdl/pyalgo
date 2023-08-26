# 104. Maximum Depth of Binary Tree
from tree_node import TreeNode


# Solution 1: Recursive / Divide and Conquer
def dfs(node) -> int:
    if not node:
        return 0
    max_depth = max(dfs(node.left)+1, dfs(node.right)+1)
    print("Node: ", node.val, "\tMax depth at node: ", max_depth)
    return max_depth


def maxDepth(root) -> int:
    return dfs(root)


# Solution 2: Traversal
class Solution:
    res = 0

    def traverse(self, node, depth) -> None:
        if not node:
            return
        depth += 1
        if (depth > self.res):
            self.res = depth

        self.traverse(node.left, depth)
        self.traverse(node.right, depth)

    def maxDepth(self, root) -> int:
        self.traverse(root, 0)
        return self.res


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    maxDepth(root)



