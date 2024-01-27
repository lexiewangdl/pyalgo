# 109.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_tree(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # Find the mid point of the linked list
        prev = slow = fast = head

        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        # Cut the linked list in between prev and slow
        if prev:
            prev.next = None

        # Now, slow is the mid point of the linked list and will be the head of tree
        root = TreeNode(slow.val)
        root.left = self.build_tree(head)
        root.right = self.build_tree(slow.next)

        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.build_tree(head)
