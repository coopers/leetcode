import heapq
from typing import List


# Time   O(N(log(N)))
# Space  O(N)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda p: p[0]**2 + p[1]**2)


# Time   O(N(log(N)))
# Space  O(N)
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]