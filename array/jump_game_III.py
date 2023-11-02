# 1306. Jump Game III
import collections
from typing import List


class Solution:
    # BFS approach
    def canReach(self, arr: List[int], start: int) -> bool:
        # Initialize queue for BFS solution
        queue = collections.deque([start])

        visited = set()  # Set to keep track of visited indices

        while len(queue) > 0:
            curr_idx = queue.popleft()

            if curr_idx in visited:
                continue
            visited.add(curr_idx)

            # if the value at current index is zero, we have found path
            if arr[curr_idx] == 0:
                return True

            # add indices we can read to the queue
            next_idx_l = curr_idx - arr[curr_idx]
            next_idx_r = curr_idx + arr[curr_idx]

            # check if these indices are valid
            if next_idx_l >= 0:
                queue.append(next_idx_l)
            if next_idx_r < len(arr):
                queue.append(next_idx_r)

        return False

