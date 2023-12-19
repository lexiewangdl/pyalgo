# 215. k-th largest element in an array
# Difficulty: Medium
import heapq
from typing import List


class Solution:
    # Optimized solution
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a heap to store the k largest elements
        heap = []

        for n in nums:
            # Add number to heap
            heapq.heappush(heap, (n, n))

            # If the size of heap exceeds k, then remove the smallest item
            if len(heap) > k:
                heapq.heappop(heap)

        # The smallest element in heap is the k-th largest element
        return heapq.heappop(heap)[1]

    # Solution using a higher space complexity
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, (-n, n))

        # Find the k-th largest element
        val = (-1, -1)
        for i in range(k):
            val = heapq.heappop(heap)

        return val[1]
