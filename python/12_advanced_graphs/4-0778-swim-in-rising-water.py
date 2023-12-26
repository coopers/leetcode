from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DIRECTIONS = ((1,0), (-1,0), (0,1), (0,-1))
        minH = [(grid[0][0], 0, 0)]
        res = 0
        while minH:
            val, row, col = heapq.heappop(minH)
            if grid[row][col] > -1:
                res = max(res, val)
                if N - 1 == row == col:
                    return res
                grid[row][col] = -1
                for dr, dc in DIRECTIONS:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < N and
                        0 <= c < N and
                        grid[r][c] > -1
                    ):
                        heapq.heappush(minH, (grid[r][c], r, c))
