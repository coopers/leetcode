import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, start_node: int) -> int:
        edges = [[] for _ in range(n + 1)]
        for origin, destination, distance in times:
            edges[origin].append((distance, destination))

        h = [(0, start_node)]
        remaining = {i for i in range(1, n + 1)}
        while h:
            distance, node = heapq.heappop(h)
            if node in remaining:
                remaining.remove(node)
                if not remaining:
                    return distance
                for d, n in edges[node]:
                    if n in remaining:
                        heapq.heappush(h, (distance + d, n))
        return -1