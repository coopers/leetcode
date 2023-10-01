from typing import List
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        GATE, INF = 0, 2147483647
        ROWS, COLS = len(rooms), len(rooms[0])
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque([(r, c) for r in range(ROWS) for c in range(COLS)
                    if rooms[r][c] == GATE])
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if (
                        0 <= row < ROWS and
                        0 <= col < COLS and
                        rooms[row][col] == INF
                    ):
                        rooms[row][col] = rooms[r][c] + 1
                        q.append((row, col))