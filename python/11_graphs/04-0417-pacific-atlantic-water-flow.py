from typing import List


# Time:  O(RC)
# Space: O(RC) the size of the call stack if every cell is greater than the last
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, s, h):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                (r, c) not in s and
                heights[r][c] >= h
            ):
                s.add((r, c))
                dfs(r + 1, c, s, heights[r][c])
                dfs(r - 1, c, s, heights[r][c])
                dfs(r, c + 1, s, heights[r][c])
                dfs(r, c - 1, s, heights[r][c])

        for r in range(ROWS):
            for c, s in [(0, pacific), (COLS - 1, atlantic)]:
                dfs(r, c, s, heights[r][c])

        for r, s in [(0, pacific), (ROWS - 1, atlantic)]:
            for c in range(COLS):
                dfs(r, c, s, heights[r][c])

        return [(r, c) for r in range(ROWS) for c in range(COLS)
                if (r, c) in pacific and (r, c) in atlantic]
    
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        MOVES = ((1,0),(-1,0),(0,1),(0,-1))
        TOP = {(0,c) for c in range(COLS)}
        BOTTOM = {(ROWS-1,c) for c in range(COLS)}
        LEFT = {(r,0) for r in range(ROWS)}
        RIGHT = {(r,COLS-1) for r in range(ROWS)}
        def dfs(r, c, h, s):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                (r, c) not in s and
                heights[r][c] >= h
            ):
                s.add((r, c))
                for dr, dc in MOVES:
                    dfs(r+dr, c+dc, heights[r][c], s)

        pacific = set()
        for r, c in TOP | LEFT:
            dfs(r, c, heights[r][c], pacific)

        atlantic = set()
        for r, c in BOTTOM | RIGHT:
            dfs(r, c, heights[r][c], atlantic)
        
        return atlantic & pacific
