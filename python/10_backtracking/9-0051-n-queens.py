from typing import List


# Time:  O(N!)
# Space: O(N^2)
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
                    p, ne = r + c, r - c
                    if col[c] and pos[p] and neg[ne]:
                        board[r][c] = "Q"
                        col[c] = pos[p] = neg[ne] = False
                        backtrack(r + 1)
                        board[r][c] = '.'
                        col[c] = pos[p] = neg[ne] = True

        backtrack(0)
        return res
