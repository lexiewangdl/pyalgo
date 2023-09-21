from typing import Optional
from list_node import ListNode


class IterativeSolution:

    # Iterative solution
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        for i in range(1, left):
            prev = prev.next
        # here, prev should point to final node of leading linked list

        curr = prev.next

        for i in range(left, right):
            ptr = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = ptr

        return dummy.next


class Solution:
    def reverseFrontK(self, node, k):
        if k == 1 or not node or not node.next:
            return node

        # recursive call
        reversed_head = self.reverseFrontK(node.next, k - 1)

        # processing
        tail = node.next.next
        node.next.next = node
        node.next = tail
        return reversed_head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        if left == 1:
            return self.reverseFrontK(head, right - left + 1)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)

        return head


class MyOriginalSolution:
    def reverseFrontK(self, node, k):
        """
        This function reverses the first k nodes of a linked list.
        :param node: Head node of linked list
        :param k: Number of nodes to reverse, starting from head node.
        :return: The head node of reversed linked list.
        """
        if k == 1 or not node or not node.next:
            return node

        # recursive call
        reversed_head = self.reverseFrontK(node.next, k-1)

        # processing
        tail = node.next.next
        node.next.next = node
        node.next = tail
        return reversed_head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        # pointer to current node
        curr = head

        # if the first node of linked list is what we want to reverse
        # then, call reverseFrontK() function and return the reversed list
        if left == 1:
            return self.reverseFrontK(head, right - left + 1)
        # Note: self.reverseFrontK(head, right - left + 1) gives us head of reversed linked list

        else:
            # move curr pointer to the node before the node we want to reverse
            for i in range(1, left-1):
                curr = curr.next
            front = curr  # front is the node before the node we want to reverse, store it in a variable

            # call reverseFrontK() function and store the head of reversed linked list
            reversed_list = self.reverseFrontK(curr.next, right - left + 1)
            # make the front node point to the head of reversed linked list
            front.next = reversed_list

        # Return the head of original linked list
        return head
