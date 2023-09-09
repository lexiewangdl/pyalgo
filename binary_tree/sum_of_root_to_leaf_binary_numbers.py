# 1022. Sum of Root To Leaf Binary Numbers
from tree_node import TreeNode
from typing import Optional, List


class Solution:
    numbers = []

    def dfs(self, node: TreeNode, num: str) -> None:
        if not node:
            return

        num += str(node.val)

        if not node.left and not node.right:
            self.numbers.append(num)
            return

        self.dfs(node.left, num)
        self.dfs(node.right, num)

        return

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.numbers = []
        self.dfs(root, "")

        res = 0
        for number in self.numbers:
            power = 0
            idx = len(number) - 1
            while idx >= 0:
                res += int(number[idx]) * pow(2, power)
                idx -= 1
                power += 1

        return res


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))
    s.sumRootToLeaf(t)

