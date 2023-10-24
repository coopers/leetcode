import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if sum(map(lambda p: math.ceil(p/mid), piles)) > h:
                left = mid + 1
            else:
                right = mid
        return left
