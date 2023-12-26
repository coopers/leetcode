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


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        GATE, INF = 0, 2147483647
        ROWS, COLS = len(rooms), len(rooms[0])
        gates = [(r, c) for r in range(ROWS) for c in range(COLS) if rooms[r][c] == GATE]
        q = deque(gates)
        distance = 0
        while q:
            distance += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    row, col = r + dr, c + dc
                    if (
                        0 <= row < ROWS and
                        0 <= col < COLS and
                        rooms[row][col] == INF
                    ):
                        rooms[row][col] = distance
                        q.append((row, col))