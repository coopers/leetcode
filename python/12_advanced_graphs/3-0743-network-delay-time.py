import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for src, dst, time in times:
            edges[src].append((time, dst))

        minHeap = [(0, k)]
        remaining = {i for i in range(1, n+1)}
        while minHeap:
            time1, src = heapq.heappop(minHeap)
            if src in remaining:
                remaining.remove(src)
                if not remaining:
                    return time1
                for time2, dst in edges[src]:
                    if dst in remaining:
                        heapq.heappush(minHeap, (time1 + time2, dst))

        return -1