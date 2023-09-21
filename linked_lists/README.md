# Linked List Problems

**Table of Contents**
- 206 - 🚩 Reverse Linked List 🍏
- 92 - 🚩 [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description/) 🍊

### 206. Reverse Linked List

#### (a) Iterative solution:
- Store the tail of the reversed linked list (of type `ListNode`)
- Initialize tail of reversed linked list to be `None`
- Use one pointer `head`, pointing to the head node in the unprocessed part of linked list
- While there are still unprocessed nodes, do the following...
  - Store the new unprocessed part of linked list as a temp variable `temp = head.next` 
    - This is because if we don't store the new unprocessed part, we will lose track of it, and we won't be able to move on to the next node
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
  - Another way to think about this is ...
  - (1) the reversed version of an empty linked list is also an **empty linked list**
  - (2) the reversed version of a **linked list with only one node** is **itself**
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

#### Summary
**What does our recursive function do?**
`reverseList()` takes the head of a linked list as input, and returns the
head node of reversed version of itself.

Iterative solution is more efficient than recursive solution.
For both solutions, time complexity is O(n). However, iterative solution has O(1) space complexity,
whereas recursive solution has O(n) space complexity (because of the **call stack**).

### 92. [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description/) (Medium)

The basic idea is that, since we are reversing all nodes from position `left` to position `right`, we need to
save the node to the left of `left`, save the node to the right of `right`, and then reverse the middle part. Finally,
connect the three parts back together.

- **Leading linked list:** The sub-chain to the left of `left` that is not going to be reversed.
- **Trailing linked list:** The tail at the end, which is not going to be reversed.


#### (a) Iterative Solution:
- Use one `for` loop to find the final node of leading linked list
- Use another `for` loop to reverse the middle part
- Return modified linked list
- Note: best to use a **dummy** node, which helps simplify edge cases

1. If `left == right`, return `head`, because if the part to be reversed contains only 1 node, we don't need to do anything
2. Initialize dummy node, which helps simplify edge cases:
  ```python
  dummy = ListNode(-1)
  dummy.next = head
  ```
3. Initialize `prev`, `prev = dummy`
4. First for loop: `for i in range(1, left): prev = prev.next`
5. Here, `prev` should be pointing to the **final node in leading linked list**
6. Next, reverse the nodes with another for loop
```python
curr = prev.next

for i in range(left, right):
    ptr = prev.next
    prev.next = curr.next
    curr.next = curr.next.next
    prev.next.next = ptr
```
7. Finally, return `dummy.next`

**How does the reversion work?**
- To reverse the nodes from `left` to `right` inclusive, it takes `right - left` steps
- At each step, what we are doing is simply:
  - Current node is first node to be reversed
  - Make the final node of leading linked list point to the next node of current node
  - Make current node's next pointer point to remainder of linked list (not yet processed)
  - Connect these two nodes in reverse direction
```bash
left = 2, right = 4

# After executing: ptr = prev.next
prev
|
1 -> 2 -> 3 -> 4 -> 5
     | 
 ptr, curr
 
# After executing: prev.next = curr.next
prev   ptr, curr
|     /
1    2 -> 3 -> 4 -> 5
|_________| 

# After executing: curr.next = curr.next.next
curr is 2, curr.next.next is 4,
now curr.next is 4

prev   ____>___ 
|     /        |                              2 --\
1    2    3 -> 4 -> 5    -- same as -->  1 -> 3 -> 4 -> 5
|____>____| 

# After executing: prev.next.next = ptr
prev is 1
ptr is 2, curr is 2

prev     ptr
|         |
1 -> 3 -> 2 -> 4 -> 5
```

#### (b) Recursive Solution:

To reverse the middle part (part to be reversed), we can travel to the end of the leading linked list (final node of leading linked list), 
save this node. Then, start reversing on the next node.

We can reverse the middle part and save the trailing part in one step, using a helper function called 
`reverseFrontK()`. This function will reverse the first `k` nodes in a linked list.
```python
def reverseFrontK(node: ListNode, k: int) -> ListNode:
    if k == 1:  # current node is only node in linked list
        return node  # the reverse of a single-node linked list is itself

    reversed_head = reverseFrontK(node.next, k-1)  # decrement k as we move to next
    
    tail = node.next.next  # node.next is final node in reversed LL
                           # node.next.next is the head node of trailing part
    node.next.next = node  # put current node at the end of reversed LL
    node.next = tail  # make current node point to trailing part

    return reversed_head  # return head of reversed linked list
```

With this helper function, we can simply do the following:
```python
  def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
      # If the part to be reversed contains only 1 node, no need to process
      if left == right:
          return head

      # If there is no leading part
      if left == 1:
          return reverseFrontK(head, right - left + 1)

      # travel to the next node while we haven't reached the first node to be reversed
      head.next = reverseBetween(head.next, left - 1, right - 1)

      return head
```










