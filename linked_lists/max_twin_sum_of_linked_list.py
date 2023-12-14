# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle point of a linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now, slow is pointing to the beginning of the second half of the linked list
        # Reverse the second half of the linked list
        curr = slow
        nxt = curr.next
        end = None

        while curr:
            curr.next = end
            end = curr
            if nxt:
                curr = nxt
                nxt = nxt.next
            else:
                break

        # Finally, find the maximum twin sum
        l = head
        r = curr

        max_twin_sum = -math.inf

        while r:
            max_twin_sum = max(l.val + r.val, max_twin_sum)
            l = l.next
            r = r.next

        return max_twin_sum
