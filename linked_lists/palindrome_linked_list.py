# 234. Palindrome Linked List
from typing import Optional
from list_node import ListNode


# My Solution 2: Use fast and slow pointers to find the mid-point of linked list
# Reverse the latter half
class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast:
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next

        reversed_latter_half = self.reverse(slow)

        p1 = head
        p2 = reversed_latter_half

        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

# My Solution 1
class MySolution:
    forward = ""
    backward = ""

    def traverse(self, node):
        if not node:
            return

        # pre-order processing
        self.forward += str(node.val)

        self.traverse(node.next)

        # post-order processing
        self.backward += str(node.val)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.forward = ""
        self.backward = ""

        self.traverse(head)

        return self.forward == self.backward