from typing import List
import heapq
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        mst_cost = 0
        remaining = {i for i in range(N)}
        distance = [math.inf] * N
        distance[0] = 0
        for _ in range(N):
            min_edge, node = math.inf, -1
            for n in remaining:
                if distance[n] < min_edge:
                    min_edge, node = distance[n], n
            
            mst_cost += min_edge
            remaining.remove(node)
            for n in remaining:
                distance[n] = min(
                    distance[n],
                    abs(points[n][0] - points[node][0]) + abs(points[n][1] - points[node][1])
                )
        
        return mst_cost


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        mst_cost = 0
        remaining = {i for i in range(N)}
        distance = [math.inf] * N
        distance[0] = 0
        for _ in range(N):
            i = min(remaining, key=lambda n: distance[n])
            mst_cost += distance[i]
            remaining.remove(i)
            for j in remaining:
                distance[j] = min(
                    distance[j],
                    abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                )
        
        return mst_cost


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return abs(x1 - x2) + abs(y1 - y2)

        N = len(points)
        remaining = {i for i in range(N)}
        h = [(0, 0)]
        res = 0
        for _ in range(N):
            while True:
                d, i = heapq.heappop(h)
                if i in remaining:
                    remaining.remove(i)
                    res += d
                    for j in remaining:
                        heapq.heappush(h, (distance(i, j), j))
                    break
        return res



