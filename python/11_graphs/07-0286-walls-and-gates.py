from typing import List
from collections import deque


# Time:  O(RC)
# Space: O(RC)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        GATE, EMPTY = 0, 2147483647
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque((r, c) for r in range(ROWS) for c in range(COLS)
                    if rooms[r][c] == GATE)
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in DIRECTIONS:
                    r, c = row + dr, col + dc
                    if (
                        0 <= r < ROWS and
                        0 <= c < COLS and
                        rooms[r][c] == EMPTY
                    ):
                        rooms[r][c] = rooms[row][col] + 1
                        q.append((r, c))