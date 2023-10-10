from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c, prev):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev:
                return 0
            if dp[r][c]:
                return dp[r][c]

            n = 1
            n = max(n, 1 + dfs(r + 1, c, matrix[r][c]))
            n = max(n, 1 + dfs(r - 1, c, matrix[r][c]))
            n = max(n, 1 + dfs(r, c + 1, matrix[r][c]))
            n = max(n, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[r][c] = n
            return n

        res = 1
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        
        return res