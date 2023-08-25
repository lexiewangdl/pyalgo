# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head or not head.next:
        return head

    p1 = head
    p2 = head.next

    while p2:
        if p2.val == p1.val:
            if not p2.next:  # if p2 is last node in linked list
                p1.next = None  # delete p2 from linked list
                return head
            p2 = p2.next  # p2 is a duplicate, ignore it
        else:  # found another unique element
            p1.next = p2  # connect p1 and p2 (same as deleting everything in between)
            p1 = p1.next
            p2 = p2.next

    return head
