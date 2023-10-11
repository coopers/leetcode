from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = 0
        x, y, z = target
        for u, v, w in triplets:
            if u <= x and v <= y and w <= z:
                a, b, c = map(max, ((a, u), (b, v), (c, w)))
            if a == x and b == y and c == z:
                return True
        return False