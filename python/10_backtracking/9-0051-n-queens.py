from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [True] * n
        pos = [True] * (2 * n - 1)
        neg = [True] * (2 * n - 1)
        board = [['.'] * n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
            else:
                for c in range(n):
                    if col[c] and pos[r + c] and neg[r - c]:
                        board[r][c] = "Q"
                        col[c] = pos[r + c] = neg[r - c] = False
                        backtrack(r + 1)
                        board[r][c] = '.'
                        col[c] = pos[r + c] = neg[r - c] = True

        backtrack(0)
        return res
