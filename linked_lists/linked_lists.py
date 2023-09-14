# 206. Reverse Linked List
from typing import Optional
from list_node import ListNode


# Iterative solution
class Solution:

    # Iterative solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None

        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp

        return tail
