from typing import List


# Time:  O(RC)
# Space: O(RC) the size of the call stack if every cell is 'O'
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == 'O'
            ):
                board[r][c] = ''
                for (dr, dc) in ((1,0), (-1,0), (0,1), (0,-1)):
                    row, col = r + dr, c + dc
                    dfs(row, col)

        for r in (0, ROWS - 1):
            for c in range(COLS):
                dfs(r, c)
        
        for r in range(ROWS):
            for c in (0, COLS - 1):
                dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = 'O' if board[r][c] == '' else 'X'