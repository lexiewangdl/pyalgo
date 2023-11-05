# 36. Valid Sudoku
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep track of existing elements in each column, row, and 3 x 3 grid
        rows = [set() for i in range(len(board))]
        columns = [set() for i in range(len(board[0]))]
        grids = [[set() for i in range(0, 3)] for i in range(0, 3)]

        # use nested for loops
        for i in range(len(board)):
            for j in range(len(board[0])):
                item = board[i][j]

                if item == '.':
                    continue

                # add to row
                if item in rows[i]:
                    return False
                else:
                    rows[i].add(item)

                # add to col
                if item in columns[j]:
                    return False
                else:
                    columns[j].add(item)

                # add to grid
                if item in grids[i // 3][j // 3]:
                    return False
                else:
                    grids[i // 3][j // 3].add(item)

        return True

