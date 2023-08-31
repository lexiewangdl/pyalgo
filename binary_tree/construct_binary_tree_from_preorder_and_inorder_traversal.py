# 105. Construct Binary Tree from Preorder and Inorder Traversal
from tree_node import TreeNode

# Optimize runtime
class Solution:
    preorder_idx = 0
    inorder_map = dict()

    def buildNode(self, preorder: list, inorder: list,
                  left: int, right: int) -> TreeNode:
        if left >= right or self.preorder_idx >= len(preorder):
            return None

        # find the index of node value in inorder
        node_val_idx = self.inorder_map[preorder[self.preorder_idx]]

        node = TreeNode(preorder[self.preorder_idx])
        self.preorder_idx += 1

        # recurse
        node.left = self.buildNode(preorder, inorder, left, node_val_idx)
        node.right = self.buildNode(preorder, inorder, node_val_idx+1, right)

        return node

    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        self.preorder_idx = 0
        self.inorder_map = dict()

        for i in range(len(inorder)):
            self.inorder_map[inorder[i]] = i

        return self.buildNode(preorder, inorder, 0, len(inorder))


# Initial solution
class Solution:
    preorder_idx = 0

    def buildNode(self, preorder: list, inorder: list,
                  left: int, right: int) -> TreeNode:
        if left == right or self.preorder_idx >= len(preorder):
            return None

        # find the index of node value (preorder[0]) in inorder
        node_val_idx = -1
        for i in range(left, right):
            if inorder[i] == preorder[self.preorder_idx]:
                node_val_idx = i
                break


        node = TreeNode(preorder[self.preorder_idx])
        self.preorder_idx += 1

        # recurse
        node.left = self.buildNode(preorder, inorder, left, node_val_idx)
        node.right = self.buildNode(preorder, inorder, node_val_idx+1, right)

        return node

    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        self.preorder_idx = 0

        return self.buildNode(preorder, inorder, 0, len(inorder))

