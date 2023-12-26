from typing import List
from collections import deque


# Time:  O(RC)
# Space: O(RC)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        FRESH, ROTTEN = 1, 2
        rotten = deque((r, c) for r in range(ROWS) for c in range(COLS)
                    if grid[r][c] == ROTTEN)
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
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 2]
        q = deque(rotten)
        minutes = 0
        while q:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    row, col = r + dr, c + dc
                    if (
                        0 <= row < ROWS and
                        0 <= col < COLS and
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))

        if any(grid[r][c] == 1 for r in range(ROWS) for c in range(COLS)):
            return -1

        return minutes if not minutes else minutes - 1