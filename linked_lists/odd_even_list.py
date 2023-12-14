# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        o = head
        e = head.next
        head_2 = e

        while e and e.next:
            # re-connect nodes
            o.next = e.next
            e.next = e.next.next

            # move pointers and connect the odd half and the even half
            o = o.next
            o.next = head_2
            e = e.next

        return head