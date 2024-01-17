import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            if sum(math.ceil(p/m) for p in piles) <= h:
                r = m
            else:
                l = m + 1

        return l
