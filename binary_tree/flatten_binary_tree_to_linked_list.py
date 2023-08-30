# 114. Flatten Binary Tree to Linked List

# Cleaned
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            curr.right = root.right
            root.right = root.left

        root.left = None

# Initial
# class Solution:
#     def help(self, node):
#         if not node:
#             return
#
#         self.help(node.left)
#         self.help(node.right)
#
#         if node.left:
#             # find last node in left subtree
#             curr = node.left
#             while curr.right:
#                 curr = curr.right
#             # append right subtree to left subtree
#             curr.right = node.right
#             # set left subtree to be right subtree
#             node.right = node.left
#
#         node.left = None
#
#     def flatten(self, root) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         self.help(root)
