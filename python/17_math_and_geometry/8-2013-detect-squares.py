from typing import List
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        return sum(
            self.ptsCount[(x, py)] * self.ptsCount[(px, y)] * self.ptsCount[(x, y)]
            for x, y in self.ptsCount.keys()
            if (
                abs(py - y) == abs(px - x) and 
                x != px and
                (x, py) in self.ptsCount and
                (px, y) in self.ptsCount
            )
        )