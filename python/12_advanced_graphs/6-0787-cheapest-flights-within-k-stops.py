from typing import List
import math


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