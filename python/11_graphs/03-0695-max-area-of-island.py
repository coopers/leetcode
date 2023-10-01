from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                grid[r][c] = 0
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return 0

        return max([dfs(r, c) for r in range(ROWS) for c in range(COLS)])
