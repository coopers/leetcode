from collections import deque
from typing import List
import math


# Bellman Ford
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [math.inf] * n
        prices[src] = 0
        for _ in range(k + 1):
            nextPrices = prices.copy()
            for s, d, p in flights:
                nextPrices[d] = min(nextPrices[d], prices[s] + p)
            prices = nextPrices
        return -1 if prices[dst] == math.inf else prices[dst]

# BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for source, destination, price in flights:
            adj[source].append((destination, price))
        
        cheapest = [math.inf] * n
        cheapest[src] = 0
        q = deque([(src, 0)])
        for _ in range(k + 1):
            for _ in range(len(q)):
                source, price_source = q.popleft()
                for destination, price_destination in adj[source]:
                    newprice = price_source + price_destination
                    if newprice < cheapest[destination]:
                        cheapest[destination] = newprice
                        q.append((destination, newprice))
        return -1 if cheapest[dst] == math.inf else cheapest[dst]