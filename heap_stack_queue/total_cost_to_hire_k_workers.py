# 2462. Total Cost to Hire K Workers
# Difficulty: Medium
import heapq
import math
from typing import List


class Solution:
    # Even better
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = 0
        right = len(costs) - 1

        l_heap = []
        r_heap = []

        cost = 0

        for i in range(k):
            while len(l_heap) < candidates and left <= right:
                heapq.heappush(l_heap, costs[left])
                left += 1

            while len(r_heap) < candidates and right >= left:
                heapq.heappush(r_heap, costs[right])
                right -= 1

            # Select the optimal candidate
            c1 = l_heap[0] if l_heap else math.inf
            c2 = r_heap[0] if r_heap else math.inf

            if c1 <= c2:
                cost += c1
                heapq.heappop(l_heap)
            else:
                cost += c2
                heapq.heappop(r_heap)

        return cost

    # Optimized my solution
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Initialize heap
        # The size of heap should always be less than or equal to 2 * candidates
        heap = []

        # Calculate total cost
        cost = 0

        # Keep track of candidate bounds
        left = 0  # next element to add to heap in left part
        right = len(costs) - 1  # next element to add to heap in right part

        # Add initial elements to heap
        for i in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[left], left))
                left += 1

            if right >= left:
                heapq.heappush(heap, (costs[right], right))
                right -= 1

        # Run k sessions to hire k workers in total
        for i in range(k):

            # If heap is empty
            if not heap:
                return cost

            # Select the cheapest worker
            c, wid = heapq.heappop(heap)
            cost += c

            if left > right:
                continue

            # Decide which candidate to add to heap
            nxt = -1
            if wid <= left:
                nxt = left
                left += 1
            elif wid >= right:
                nxt = right
                right -= 1

            # Add the next candidate to heap
            heapq.heappush(heap, (costs[nxt], nxt))

        return cost

    # # My initial solution
    # def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    #     # Initialize heap
    #     # The size of heap should always be less than or equal to 2 * candidates
    #     heap = []

    #     # Calculate total cost
    #     cost = 0

    #     # Keep track of candidates already added to heap
    #     interviewed = set()

    #     cand_idx = set()

    #     # Add initial elements to heap
    #     for j in range(candidates):

    #         if j < len(costs):
    #             cand_idx.add(j)

    #         if len(costs)-1-j >= 0:
    #             cand_idx.add(len(costs)-1-j)

    #     interviewed = interviewed.union(cand_idx)

    #     for item in cand_idx:
    #         heapq.heappush(heap, (costs[item], item))

    #     # Keep track of candidate bounds
    #     left = candidates - 1
    #     right = len(costs) - candidates

    #     # Run k sessions to hire k workers in total
    #     for i in range(k):

    #         # Select the cheapest worker
    #         c, wid = heapq.heappop(heap)
    #         cost += c

    #         if left >= right:
    #             continue

    #         # Decide which candidate to add to heap
    #         nxt = -1
    #         if wid <= left:
    #             nxt = left + 1
    #             left += 1
    #         elif wid >= right:
    #             nxt = right - 1
    #             right -= 1

    #         # Add the next candidate to heap
    #         if nxt not in interviewed:
    #             heapq.heappush(heap, (costs[nxt], nxt))
    #             interviewed.add(nxt)

    #     return cost