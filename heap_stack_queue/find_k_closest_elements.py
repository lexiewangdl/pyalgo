# 658. Find k Closest Elements
import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []

        # Add all elements to heap
        for i in range(len(arr)):
            heapq.heappush(h, (abs(x - arr[i]), arr[i]))  # (priority, item)

        result = []
        while len(result) < k:
            result.append(heapq.heappop(h)[1])

        # Sort items in ascending order
        result.sort()

        return result

    def findClosestElements_2(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap, max_heap = [], []

        # Add all elements to heap
        for i in range(len(arr)):
            if arr[i] < x:
                # max_heap stores values that are less than x
                heapq.heappush(max_heap, (-arr[i]))
            else:
                # min_heap stores values that are greater than x
                heapq.heappush(min_heap, (arr[i]))

        # Remove elements from heap
        result = []
        while len(result) < k:
            if min_heap and max_heap:
                if x + max_heap[0] <= min_heap[0] - x:
                    result.append(-heapq.heappop(max_heap))
                else:
                    result.append(heapq.heappop(min_heap))
            elif max_heap:
                result.append(-heapq.heappop(max_heap))
            else:
                result.append(heapq.heappop(min_heap))

        result.sort()

        return result