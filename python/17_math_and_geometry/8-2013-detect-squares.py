from typing import List
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        return sum(
            self.ptsCount[(x, y)] * self.ptsCount[(x, y0)] * self.ptsCount[(x0, y)]
            for x, y in self.ptsCount.keys()
            if (
                abs(y - y0) == abs(x - x0) and 
                x != x0 and
                (x, y0) in self.ptsCount and
                (x0, y) in self.ptsCount
            )
        )