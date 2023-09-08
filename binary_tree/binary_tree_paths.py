# 257. Binary Tree Paths
from typing import Optional, List
from tree_node import TreeNode


class Solution:
    ans = []

    def dfs(self, node, path):
        if not node:
            return

        if path == "":
            path += f"{node.val}"
        else:
            path += f"->{node.val}"

        if not node.left and not node.right:
            self.ans.append(path)
            return

        self.dfs(node.left, path)
        self.dfs(node.right, path)

        return

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.dfs(root, "")
        return list(self.ans)

