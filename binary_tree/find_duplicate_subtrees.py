# 652. Find Duplicate Subtrees (Medium)
from tree_node import TreeNode
from collections import Counter


# My solution 2 (looks cleaner)
class Solution:
    c = {}
    result = []

    def represent_subtree(self, node) -> str:
        if not node:
            return " "  # use whitespace to represent null node

        # recurse, then, post-order processing
        # use , to differentiate nodes
        curr_subtree_nodes = self.represent_subtree(node.left) + "," + self.represent_subtree(node.right) + "," + str(node.val) + ","

        # check if current subtree is a duplicate
        self.c[curr_subtree_nodes] += 1
        if self.c[curr_subtree_nodes] == 2:  # seen one subtree with same structure 
            self.result.append(node)

        return curr_subtree_nodes

    def findDuplicateSubtrees(self, root: TreeNode) -> list:
        self.c = Counter()
        self.result = list()

        self.represent_subtree(root)

        return self.result


# My solution 1
class Solution:
    subtrees = dict()
    result = list()

    def represent_subtree(self, node) -> str:
        if not node:
            return " "  # use whitespace to represent null node

        # recurse
        left_subtree_nodes = self.represent_subtree(node.left)
        right_subtree_nodes = self.represent_subtree(node.right)

        # post-order processing
        # use , to differentiate nodes
        curr_subtree_nodes = left_subtree_nodes + "," + right_subtree_nodes + "," + str(node.val) + ","

        # check if current subtree is a duplicate
        num_seen = self.subtrees.get(curr_subtree_nodes, 0)
        if num_seen == 1:  # seen one subtree with same structure
            self.result.append(node)
        self.subtrees[curr_subtree_nodes] = num_seen + 1

        return curr_subtree_nodes

    def findDuplicateSubtrees(self, root: TreeNode) -> list:
        self.subtrees = dict()
        self.result = list()

        self.represent_subtree(root)

        return self.result
