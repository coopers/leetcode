import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for src, dst, time in times:
            edges[src].append((time, dst))

        minHeap = [(0, k)]
        best_times = [math.inf] * (n + 1)
        remaining = {i for i in range(1, n + 1)}
        while minHeap:
            time1, src = heapq.heappop(minHeap)
            if src in remaining:
                remaining.remove(src)
                if not remaining:
                    return time1
                for time2, dst in edges[src]:
                    if dst in remaining:
                        t = time1 + time2
                        if t < best_times[dst]:
                            best_times[dst] = t
                            heapq.heappush(minHeap, (t, dst))

        return -1
    

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for src, dst, time in times:
            edges[src].append((time, dst))

        best_times = [math.inf] * (n + 1)
        best_times[k] = 0
        remaining = {i for i in range(1, n + 1)}
        for _ in range(n):
            t, i = math.inf, -1
            for node in remaining:
                if best_times[node] < t:
                    t, i = best_times[node], node

            if i == -1:
                return -1
            
            remaining.remove(i)
            for time, j in edges[i]:
                if j in remaining:
                    best_times[j] = min(best_times[j], time + t)

        m = max(best_times[1:])
        return -1 if m == math.inf else m