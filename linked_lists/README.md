# Linked List Problems

**Table of Contents**
- 206 - 🚩 Reverse Linked List 🍏

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

**When to perform processing? Before or after recursive call?** Since this problem asks for reversed linked list,
it's intuitive to think that the problem should be solved bottom-up, i.e. from the last node to the head node. Thus, 
perform processing _after_ recursive call (similar to _post-order_ processing for trees).

**What should the recursive function return?** The problem asks for reversed linked list,
we can make the recursive function return _head node_ of reversed linked list.

**For each recursive call, what needs to be done?**
- If current node `head` is null, or if current node's next pointer points to null, return current node
  - This takes care of two situations: 
  - (1) input linked list is empty linked list, with an empty head node, the reversed version of itself is also a null node, just return null
  - (2) if we have reached the last node in linked list, the current node would be the head node of our reversed linked list, return this node (we will make sure its next pointer and its following nodes' next pointers point to correct things while we do processing)
- Recursive call, `reversed_head = reverseList(head.next)`
  - Since recursive function call _precedes_ processing of input node, we will _reach the final node in input linked list_ first
  - Assume that the returned node is the _head of reversed linked list_
- Process input node `head`
  - Assuming that we already have `reversed_head`, which is head of reversed linked list
  - `reversed_head` is what we need to return
  - However, we must make sure that current node `head` is correctly appended to the reversed linked list
  - Problem is, which node is the tail of reversed linked list?
  - The answer is `head.next.next`, but why?
  - `head.next` is the final non-null node in reversed linked list
  - `head.next.next` is the null node or _empty spot_ at the end of the reversed linked list
  - Thus, set current node to be `head.next.next`, and then set `head.next` to null (avoid forming a cycle)
  ```bash
  # input linked list
  1 -> 2 -> 3 -> 4 -> 5
  
  # processing node 5
  1 -> 2 -> 3 -> 4 -> 5
                      |
                    head, reversed_head
  
  # processing node 4
                  reversed_head
                      |
  1 -> 2 -> 3 -> 4 -> 5 -> None -- head.next.next
                 |    |
                head  head.next
  
      # set head.next.next = head, and head.next = None
      1 -> 2 -> 3  # to-be-reversed part
                 \
             5 -> 4 -> None  # reversed part
             |    |
  reversed_head   head    
  
  # processing node 3
               head
                |
      1 -> 2 -> 3
                 \
             5 -> 4 -> None -- head.next.next
             |    |
  reversed_head   head.next  
  
      # set head.next.next = head, and head.next = None
               1 -> 2 
                      \
             5 -> 4 -> 3 (head) -> None
             |    
  reversed_head   
  ```

**What does our recursive function do?**
`reverseList()` takes the head of a linked list as input, and returns the
head node of reversed version of itself.













