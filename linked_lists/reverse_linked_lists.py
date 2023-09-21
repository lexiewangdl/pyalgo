# 206. Reverse Linked List
from typing import Optional
from list_node import ListNode


# Recursive solution
class RecursiveSolution:

    # Recursive solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if empty linked list or reached final node of linked list
        if not head or not head.next:
            return head

        # travel to next node
        reversed_head = self.reverseList(head.next)

        # "post-order" processing
        head.next.next = head
        head.next = None

        return reversed_head  # head node of reversed linked list


# Iterative solution
class IterativeSolution:

    # Iterative solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None

        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp

        return tail
