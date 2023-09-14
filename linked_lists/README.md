# Linked List Problems

**Table of Contents**
- 206 - Reverse Linked List 🍏

### 206. Reverse Linked List

#### (a) Iterative solution:
- Store the tail of the reversed linked list (of type `ListNode`)
- Initialize tail of reversed linked list to be `None`
- Use one pointer `head`, pointing to the head node in the unprocessed part of linked list
- While there are still unprocessed nodes, do the following...
  - Store the new unprocessed part of linked list as a temp variable `temp = head.next`
  - Make current head (head of unprocessed part)'s `next` pointer point to `tail` (`head.next = tail`)
  - Update `tail` (note that `tail` should always point to the _first_ node), `tail = head` 
  - Update `head`, make it point to the head of new unprocessed part, `head = temp`

For example: given the linked list `1 -> 2 -> 3 -> 4 -> 5` ...
```python
# Step 1
while head:  # 1(head) -> 2 -> 3 -> 4 -> 5
    temp = head.next  # 2(temp) -> 3 -> 4 -> 5
    head.next = tail  # 1(head) -> None(tail)
    tail = head  # 1(tail) -> None
    head = temp  # 2(head) -> 3 -> 4 -> 5

# Step 2
while head:  # 2(head) -> 3 -> 4 -> 5
    temp = head.next  # 3(temp) -> 4 -> 5
    head.next = tail  # 2(head) -> 1(tail) -> None
    tail = head  # 2(tail) -> 1 -> None
    head = temp  # 3(head) -> 4 -> 5
```

#### (b) Recursive solution:

