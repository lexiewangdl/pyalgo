# 199. Binary Tree Right Side View
from tree_node import TreeNode
from typing import Optional, List


class Solution:
    view = []

    def dfs(self, node: TreeNode, level: int) -> None:
        if not node:
            return

        # pre-order processing
        if len(self.view) <= level:
            self.view.append(101)

        if self.view[level] == 101:
            self.view[level] = node.val

        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)

        return

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.view = []
        self.dfs(root, 0)
        return self.view

