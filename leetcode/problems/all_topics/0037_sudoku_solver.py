from all_import import *

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Constraints:
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit or '.'.
- It is guaranteed that the input board has only one solution.
'''

class Solution:
    from itertools import product
    
    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.search(board)
    
    def is_valid_state(self, board):
        for row in self.get_rows(board):
            if not set(row) == self.DIGITS:
                return False
        for col in self.get_cols(board):
            if not set(col) == self.DIGITS:
                return False
        for grid in self.get_grids(board):
            if not set(grid) == self.DIGITS:
                return False
        return True


    def get_candidates(self, board, row, col):
        used_digits = set()
        used_digits.update(self.get_kth_row(board, row))
        used_digits.update(self.get_kth_col(board, col))
        used_digits.update(self.get_grid_at_row_col(board, row, col))
        used_digits -= set([self.EMPTY])
        return self.DIGITS - used_digits

    def search(self, board):
        if self.is_valid_state(board):
            return True
        
        for row_idx, row in enumerate(board):
            for col_idx, elm in enumerate(row):
                if elm == self.EMPTY:
                    for candidate in self.get_candidates(board, row_idx, col_idx):
                        board[row_idx][col_idx] = candidate
                        if self.search(board):
                            return True
                        else:
                            board[row_idx][col_idx] = self.EMPTY
                    return False
        return True

    def get_kth_row(self, board, k):
        return board[k]

    def get_rows(self, board):
        for i in range(self.SHAPE):
            yield board[i]
    
    def get_kth_col(self, board, k):
        return [
            board[row][k] for row in range(self.SHAPE)
        ]

    def get_cols(self, board):
        for col in range(self.SHAPE):
            ret = [
                    board[row][col] for row in range(self.SHAPE)
            ]
            yield ret

    def get_grid_at_row_col(self, board, row, col):
        row = row // self.GRID * self.GRID
        col = col // self.GRID * self.GRID
        return [
            board[r][c] for r, c in 
            product(range(row, row + self.GRID), range(col, col + self.GRID))
        ]

    def get_grids(self, board):
        for row in range(0, self.SHAPE, self.GRID):
            for col in range(0, self.SHAPE, self.GRID):
                grid = [
                    board[r][c] for r, c in 
                    product(range(row, row + self.GRID), range(col, col + self.GRID))
                ]
                yield grid
                