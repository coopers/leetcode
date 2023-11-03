from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        FRESH, ROTTEN = 1, 2
        rotten = deque([(r, c) for r in range(ROWS) for c in range(COLS)
                    if grid[r][c] == ROTTEN])
        fresh = sum(1 for r in range(ROWS) for c in range(COLS)
                if grid[r][c] == FRESH)
        time = 0
        while rotten and fresh:
            time += 1
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for dr, dc in DIRECTIONS:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < ROWS and
                        0 <= c < COLS and
                        grid[r][c] == FRESH
                    ):
                        fresh -= 1
                        grid[r][c] = ROTTEN
                        rotten.append((r, c))

        return -1 if fresh else time