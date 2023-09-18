from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        first = last = 0
        for r in range(ROWS):
            for c in range(COLS):
                if word[0] == board[r][c]:
                    first += 1
                elif word[-1] == board[r][c]:
                    last += 1
                    
        if last < first:
            word = word[::-1]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
            ):
                return False
            
            ch = board[r][c]
            board[r][c] = ''
            i += 1
            if (
                dfs(r + 1, c, i)
                or dfs(r - 1, c, i)
                or dfs(r, c + 1, i)
                or dfs(r, c - 1, i)
            ):
                return True

            board[r][c] = ch

        return any(dfs(r, c, 0) for r in range(ROWS) for c in range(COLS))