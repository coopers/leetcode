import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while True:
            if l > r:
                return res

            m = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / m)
            if totalTime <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
