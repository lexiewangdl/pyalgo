from typing import Optional
from list_node import ListNode


class Solution:
    def reverse(self, nodeA, nodeB):
        "Reverse the nodes in between node A and node B, not including node B"
        prev = None
        curr = nodeA

        while curr != nodeB:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        A = head
        B = head
        for i in range(k):
            if not B:
                return head
            B = B.next

        front = self.reverse(A, B)
        head.next = self.reverseKGroup(B, k)

        return front

