# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    target = -1
    result = False

    # DFS
    def get_path_sum(self, node, path_sum) -> int:
        """ Find the path sum from root node to this node. """
        # base case
        if not node:
            return path_sum

        # recursive case
        # check left child

        # pre-order traversal
        new_path_sum = path_sum + node.val

        # check root-to-leaf path sum only for leaf nodes with no children
        if not node.left and not node.right and new_path_sum == self.target:
            self.result = True
            return new_path_sum

        # left child
        self.get_path_sum(node.left, new_path_sum)

        # right child
        self.get_path_sum(node.right, new_path_sum)

        return new_path_sum

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.target = targetSum
        self.result = False

        self.get_path_sum(root, 0)

        return self.result
