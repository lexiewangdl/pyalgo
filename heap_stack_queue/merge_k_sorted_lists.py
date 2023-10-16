# 23. Merge k Sorted Lists
# Hard
from heapq import heappush, heappop
from typing import List, Optional


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode(-1)
        curr = result

        # O(k log k)
        for i in range(len(lists)):  # O(k)
            if not lists[i]:
                continue
            heapq.heappush(heap, (lists[i].val, i))  # O(log k)

        while len(heap) > 0:  # O(N)
            _, i = heapq.heappop(heap)  # O(log k)
            curr.next = lists[i]
            curr = curr.next

            if curr.next:
                heapq.heappush(heap, (curr.next.val, i))
                lists[i] = curr.next

        return result.next