# 129. Sum root to leaf numbers
from typing import Optional, List
from tree_node import TreeNode


class Solution:
    nums = []

    def dfs(self, node, num) -> None:
        if not node:
            return

        num += f"{node.val}"

        if not node.left and not node.right:
            self.nums.append(num)

        self.dfs(node.left, num)
        self.dfs(node.right, num)

        return

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        self.dfs(root, "")

        res = 0
        for item in self.nums:
            res += int(item)

        return res
