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