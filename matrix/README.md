# Matrix Problems

## Table of Contents
1. BFS Questions
    1. 🚩 [1091. Shortest Path in Matrix](#1091-shortest-path-in-matrix-medium) 🍊
   2. 🚩 [864. Shortest Path to Get All Keys](#864-shortest-path-to-get-all-keys-hard) 🍎
2. DFS
3. Other


## BFS Questions

- Use a queue `q = collections.deque()` to store the nodes to be visited
- To move in different directions, define a list of directions `dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]`, depending
  on which direction you can move
- Use a matrix `visited` (or a set) to store the visited nodes, avoid vising the same node multiple times and 
  getting stuck in a loop

### 1091. [Shortest Path in Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) (Medium)

The question asks for shortest clear path, where a _clear path_ is a path on which all cells have value `0`.
In this question, length of shortest path is defined as the number of cells visited. We can move in 8 directions,
including diagonals.
So basically, we can treat `0` as a road and `1` as a wall.

Very important questions to ask:
1. Which directions can I move?
2. How to keep track of the path length?
3. **When to mark a cell as visited?** When we add it to the queue or when we pop it from the queue?

[Solution](shortest_path_in_binary_matrix.py):
- Define 8 directions
- Define start and end cells: `start = (0, 0)`, `end = (m - 1, n - 1)`
- Check for cases where the start or end cell is blocked
  - If the start cell or end cell is `1`, return -1
- Check for simplest case
  - If the start and end cells are the same, return 1
- Initialize _queue_ and _visited_ matrix
  - `q = collections.deque()`
  - `visited = [[False] * n for _ in range(m)]`
- Add start cell to queue and mark it as visited
  - Note: we always mark a cell as visited when we _add_ it to the queue, this is because we want to avoid adding
    the same cell to the queue multiple times, which will cause infinite loop; in other words, _each cell can only be
    added to the queue once_
  - `q.append((0, 0, 1))`, in our queue, each element has 3 components: _row index, column index, and distance from start_,
    in this question, distance is number of cells on the path, so we initialize it to 1
  - `visited[start[0]][start[1]] = True`
- While the queue is not empty
  - Pop the first cell from the queue, `row, col, dist = q.popleft()`
  - Use a `for` loop to check all directions, and do the following:
    - 'new_row = row + dir[0]', 'new_col = col + dir[1]
    - Check if the cell is a valid move by checking the following:
      - (1) Are the indices out of bound?
      - (2) Is the cell visited?
      - (3) Is the cell blocked? (i.e. is the cell `1`?)
    - Check if the cell is the _end cell_: if we have reached the end cell, we want to compare all path lengths
      that lead to this cell. We can't just return the first path length that we remove from queue.
      - `shortest_path_distance = math.inf` is used to keep track of the shortest path distance, this is defined outside the while loop
      - Update shortest path distance, if `dist + 1` is smaller than the current shortest path distance
    - Finally, append the cell to the queue and mark it as visited
      - `q.append((new_row, new_col, dist + 1))`
      - `visited[new_row][new_col] = True`
- Eventually, return `-1` if the shortest path distance is `math.inf`, otherwise return the shortest path distance


### 864. [Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/description/) (Hard)

Very similar to previous question, except for the following:
1. The goal is to get all keys, not to reach a specific cell
2. We can go back to a cell that we have visited before, but this is dependent on the keys we have (for example,
   if we have visited a cell with key `a`, we can walk back and take another route to open the door `A` and keep moving)

Thus, it's very important to not use a single matrix to store visited cells,
instead, use a _hashmap_ to store visited cells, where the key is a representation of _key state_ (i.e. the unique 
combination of possible keys that we have), and the value is a matrix or set that stores visited cells for that key state.

Since number of keys is in the range `[0, 6]`, we can use a string to represent key states. For example, `000000` means 
we have no key, `010000` means we have key `b`. The index of a key is determined by `ord(key) - ord('a')`.

What needs to be stored in queue? We need the row index, column index, key state, and distance from start.

[BFS Solution](shortest_path_to_get_all_keys.py):
- Define 4 directions
- Initialize _queue_ and _visited_ hashmap
  - `q = collections.deque()`
  - `visited = dict()`
- Find the start cell and total number of keys in grid, this is our goal
  - Once we found the start cell, we can add it to the queue and mark it as visited,
    `q.append((start_row, start_col, '000000', dist))` then `visited['000000'] = set((start_row, start_colu))`
    - Note: we use a string to represent key state, where `000000` means we have no key
    - Note: we mark the start cell as visited when we add it to the queue
- While the queue is not empty:
  - Pop the first cell from the queue, `row, col, key_state, dist = q.popleft()`
  - Go to all 4 directors:
    - `new_row = row + dir[0]`, `new_col = col + dir[1]`
    - Check if the cell is a valid move by checking the following:
      - (1) Are the indices out of bound?
      - (2) Is the cell visited (in the current key state)?
      - (3) Is the cell blocked? (i.e. is the cell `#`?)
      - (4) If the cell is a door, do we have the key to open it? If not, `continue`.
      - (5) If the cell is a key, is it a new key that we don't have?
        - If yes, update key state
        - Here, check if we have found all keys! If yes, return the distance
          - Note: must check if we have found all keys using new key state, i.e. `new_key_state.count('1') == all_keys_count`, must not use current key state
        - Update the `visited[new_key_state]`, maybe initialize it to an empty set
        - Add the cell to the queue and mark it as visited in new key state
      - Otherwise, just add the cell to the queue and mark it as visited in current key state, remember to update distance
- Eventually, return `-1` if we can't find all keys

