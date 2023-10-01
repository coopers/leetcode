from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = ''
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
    
        return islands


# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1'):
                        grid[r][c] = ''
                        q.append((r + 1, c))
                        q.append((r - 1, c))
                        q.append((r, c + 1))
                        q.append((r, c - 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
    
        return islands