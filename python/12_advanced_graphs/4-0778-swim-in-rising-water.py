from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        remaining = [[True] * N for _ in range(N)]
        minH = [(grid[0][0], 0, 0)]
        res = 0
        while minH:
            val, row, col = heapq.heappop(minH)
            res = max(res, val)
            if remaining[row][col]:
                if N - 1 == row == col:
                    return res
                remaining[row][col] = False
                for dr, dc in DIRECTIONS:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < N and
                        0 <= c < N and
                        remaining[r][c]
                    ):
                        heapq.heappush(minH, (grid[r][c], r, c))
