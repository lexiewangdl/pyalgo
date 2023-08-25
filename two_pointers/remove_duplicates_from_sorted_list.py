# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optimized
def deleteDuplicates(head):
    if not head or not head.next:
        return head

    p1 = head  # last unique element (p1 is unique and everything to its left is unique)
    p2 = head.next  # next element to be checked

    while p2:
        if p1.val != p2.val:  # found another unique element
            p1.next = p2  # connect p1 and p2 (same as deleting everything in between)
            p1 = p1.next
        p2 = p2.next  # otherwise, p2 is a duplicate, ignore it

    p1.next = None  # at this point, p2 has checked all nodes
    # disconnect p1 with rest of linked list, remove any trailing duplicates

    return head

# Original solution
# def deleteDuplicates(head):
#     if not head or not head.next:
#         return head
#
#     p1 = head  # last unique element (p1 is unique and everything to its left is unique)
#     p2 = head.next  # next element to be checked
#
#     while p2:
#         if p1.val != p2.val:  # found another unique element
#             p1.next = p2  # connect p1 and p2 (same as deleting everything in between)
#             p1 = p1.next
#         elif not p2.next:  # if p2 is last node in linked list
#             p1.next = None  # delete p2 from linked list
#         p2 = p2.next  # otherwise, p2 is a duplicate, ignore it
#
#     return head
