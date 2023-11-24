from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c, prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0

            if dp[r][c]:
                return dp[r][c]

            dp[r][c] = 1 + max(dfs(r + dr, c + dc, matrix[r][c]) for dr, dc in DIRS)
            return dp[r][c]
        
        return max(dfs(r, c, -1) for r in range(ROWS) for c in range(COLS))