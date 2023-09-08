# 95. Unique Binary Search Trees II
from typing import List, Optional
from tree_node import TreeNode


class Solution:
    trees = dict()

    def build(self, left: int, right: int) -> list:
        result = []

        # subtree is null
        if left > right:
            result.append(None)
            return result

        # subtree is single node
        elif left == right:
            result.append(TreeNode(left))
            return result

        if f"{left},{right}" in self.trees.keys():
            return self.trees[f"{left},{right}"]

        # subtree needs to be recursively built
        for i in range(left, right + 1):
            left_subtrees = self.build(left, i - 1)
            right_subtrees = self.build(i + 1, right)
            for l in left_subtrees:
                for r in right_subtrees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)

        self.trees[f"{left},{right}"] = result

        return result

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.trees = dict()
        return self.build(1, n)

