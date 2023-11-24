from typing import List
import math

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        remaining = {i for i in range(n)}
        min_dist = [math.inf] * n
        min_dist[0] = 0
        while remaining:
            _, node = min((min_dist[i], i) for i in remaining)            
            remaining.remove(node)
            for i in remaining:
                min_dist[i] = min(
                    min_dist[i],
                    abs(points[i][0] - points[node][0]) +\
                    abs(points[i][1] - points[node][1])
                )
        
        return sum(min_dist)