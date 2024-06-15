# Islands 

## Summary

## Practice Problems
- [200. Number of Islands](#200-number-of-islands-medium) 🍊

### 200. [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)
To find out the number of islands, iterate through the grid (using nested `for` loops).
Whenever you find a `1` (land), increment the count of islands `num_islands`, and then 
use DFS to search for surrounding lands, for every surrounding land, change it to `0` (make it
become water). Basically, we are making all discovered lands disappar. In this way, there's no need
to store a `visited` array to keep track of visited lands.

The DFS helper function is defined as follows:
- The base case is when the indices are out of range, or the cell is water (`0`). If the indices are
  out of range (i.e., `i < 0`, `i >= m`, `j < 0`, `j >= n`), return immediately. If the cell is water,
  also return, because we are only interested in turning lands into water.
- Change the cell to water by setting `grid[i][j] = '0'`.
- Recursively call the DFS function on the surrounding cells: up, down, left, and right.


