from all_import import *

'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
- 1 <= n <= 9
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.solve(n)

    def is_valid_state(self, state, n):
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        position = len(state)
        candidates = set(range(n))

        for r, c in enumerate(state):
            candidates.discard(c)
            distance = position -  r
            candidates.discard(c + distance)
            candidates.discard(c - distance)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def solve(self, n):
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def state_to_string(self, state, n):
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret
