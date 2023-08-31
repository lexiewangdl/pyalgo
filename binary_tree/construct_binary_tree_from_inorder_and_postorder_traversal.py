# 106. Construct Binary Tree from Inorder and Postorder Traversal
from tree_node import TreeNode

class Solution:
    inorder_map = dict()

    def build(self, inorder: list, postorder: list, 
              il: int, ir: int, 
              pl: int, pr: int) -> TreeNode:

        # Base case
        if il >= ir or pl >= pr:
            return None

        # build node
        node_val = postorder[pr-1]
        node = TreeNode(node_val)

        # find index of node in inorder array
        node_idx = self.inorder_map[node_val]
        # length of left subtree = node_idx - il

        # recurse
        node.left = self.build(inorder, postorder, il, node_idx, pl, pl+(node_idx-il))
        node.right = self.build(inorder, postorder, node_idx + 1, ir, pl+(node_idx-il), pr-1)

        return node

    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        # Add elements in inorder array to map
        self.inorder_map = dict()
        length = len(inorder)

        for i in range(length):
            self.inorder_map[inorder[i]] = i

        return self.build(inorder, postorder, 0, length, 0, length)