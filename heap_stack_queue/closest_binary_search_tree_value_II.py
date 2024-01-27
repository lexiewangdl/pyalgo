# 272. Closest Binary Search Tree Value II
from typing import List, Optional
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    heap = []
    target = -1

    def traverse(self, node):
        if not node:
            return

        heapq.heappush(self.heap, (abs(self.target - node.val), node.val))  # priority, value

        self.traverse(node.left)
        self.traverse(node.right)
        return

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.heap = []
        self.target = target

        # traverse the binary tree
        self.traverse(root)

        result = [heapq.heappop(self.heap)[1] for _ in range(k)]

        return result
