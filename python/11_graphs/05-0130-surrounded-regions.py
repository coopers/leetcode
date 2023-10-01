from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == 'O'
            ):
                board[r][c] = 'T'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = 'O' if board[r][c] == 'T' else 'X'
        
        return board

        
