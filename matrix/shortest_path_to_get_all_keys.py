# 864. Shortest Path to Get All Keys
# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
from typing import List
import collections


class Solution:
    def get_index_of_char(self, char: str):
        # ord() gives ascii code of char
        return ord(char) - ord('a')

    def get_new_key_state(self, key_state: str, idx_key: int):
        new_ks = key_state[:idx_key] + '1' + key_state[idx_key + 1:]
        return new_ks

    def check_has_key(self, key: str, key_state: str):
        return key_state[ord(key) - ord('a')] == '1'

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # up, left, down, right

        # my_keys = set()
        all_keys = 0

        # use a map in which the key is a key state, and value represents cells visited in this key state
        visited = dict()

        # BFS solution
        # the queue stores (i, j, key_state, distance)
        q = collections.deque([])

        # find the starting cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] in 'abcedf':
                    all_keys += 1
                if grid[i][j] == '@':
                    q.append((i, j, "000000", 0))
                    visited["000000"] = visited.get("000000", set())
                    visited["000000"].add((i, j))

        while len(q) > 0:
            r, c, key_state, dist = q.popleft()

            # check all four directions, and add to queue if valid move
            for d in directions:
                row = r + d[0]
                col = c + d[1]

                # check if within limit
                if not (0 <= row and row < m and 0 <= col and col < n):
                    continue

                if (row, col) in visited[key_state]:
                    continue

                char = grid[row][col]
                # check if new cell is a wall
                if char == '#':
                    continue
                # check if new cell contains new key
                if char.islower() and not self.check_has_key(char, key_state):
                    # add new key, update key state
                    # my_keys.add(char)
                    idx_key = self.get_index_of_char(char)
                    new_key_state = self.get_new_key_state(key_state, idx_key)

                    # if we have collected all keys, return distance + 1
                    if new_key_state.count('1') == all_keys:
                        return dist + 1

                    else:
                        # add this cell to queue, update visited
                        visited[new_key_state] = visited.get(new_key_state, set())
                        visited[new_key_state].add((row, col))
                        q.append((row, col, new_key_state, dist + 1))

                # a lock that we have no key to
                elif char.isupper() and not self.check_has_key(char.lower(), key_state):
                    # invalid move
                    continue

                # mark new cell as visited
                elif (row, col) not in visited[key_state]:
                    visited[key_state].add((row, col))
                    q.append((row, col, key_state, dist + 1))

        return -1

