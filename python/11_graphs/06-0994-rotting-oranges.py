from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH, ROTTEN = 1, 2
        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        numFresh = 0
        minutes = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    numFresh += 1
                elif grid[r][c] == ROTTEN:
                    rotten.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while numFresh > 0 and rotten:
            minutes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        0 <= row < ROWS and 
                        0 <= col < COLS and 
                        grid[row][col] == FRESH
                    ):
                        numFresh -= 1
                        grid[row][col] = ROTTEN
                        rotten.append((row, col))
        
        return -1 if numFresh else minutes