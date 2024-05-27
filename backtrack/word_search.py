# 79. Word Search
class Solution:
    word = ''
    m = 0
    n = 0
    board = []

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    result = False

    def backtrack(self, curr_row, curr_col, word_idx):
        """
        curr_row: row index of the cell currently checking
        curr_col: col index of the cell currently checking
        word_idx: index of element within word we're currently checking
        """
        # Check if we have found target word
        if word_idx >= len(self.word):
            # Found target word
            self.result = True
            return
        # If answer has been found, no need to search
        if self.result == True:
            return
        # Check if current indices are out of range
        if curr_row < 0 or curr_col < 0 or curr_row >= self.m or curr_col >= self.n:
            return
        # Check if current element has been used
        if self.board[curr_row][curr_col] == '-':  # if used[curr_row][curr_col]:
            return
        # Check if current element matches the word_idx-th element in target word
        if self.board[curr_row][curr_col] != self.word[word_idx]:
            return

        # Continue to search
        for row_dir, col_dir in self.directions:
            # Do selection
            temp = self.board[curr_row][curr_col]
            self.board[curr_row][curr_col] = '-'

            self.backtrack(curr_row + row_dir, curr_col + col_dir, word_idx + 1)

            # Undo selection
            self.board[curr_row][curr_col] = temp

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        self.word = word
        self.board = board
        self.m = len(board)
        self.n = len(board[0])

        # Initialized used matrix
        for i in range(self.m):
            for j in range(self.n):
                self.backtrack(i, j, 0)

        return self.result
