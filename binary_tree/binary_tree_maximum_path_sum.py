# 124. Binary Tree Maximum Path Sum

import math
from tree_node import TreeNode


class Solution:
    ans = 0

    def find(self, node: TreeNode) -> int:
        if not node:
            return 0

        left_sum = self.find(node.left)
        right_sum = self.find(node.right)

        max_single_path = max(node.val, left_sum + node.val, right_sum + node.val)
        path_sum = max(max_single_path, left_sum + right_sum + node.val)

        self.ans = path_sum if path_sum > self.ans else self.ans

        return max_single_path

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -math.inf
        self.find(root)
        return self.max_path_sum