import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        s = {i for i in range(len(points))}
        h = [(0, 0)]
        res = 0
        while s:
            cost, i = heapq.heappop(h)
            if i in s:
                res += cost
                s.remove(i)
                x1, y1 = points[i]
                for j in s:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(h, (dist, j))
        return res