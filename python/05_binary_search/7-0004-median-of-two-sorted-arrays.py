from typing import List
import math


# Time: log(min(n, m))
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        while True:
            a = l + (r - l) // 2
            b = half - a - 2
            aL = A[a] if a >= 0 else -math.inf
            bL = B[b] if b >= 0 else -math.inf
            aR = A[a + 1] if (a + 1) < len(A) else math.inf
            bR = B[b + 1] if (b + 1) < len(B) else math.inf
            # partition is correct
            if aL <= bR and bL <= aR:
                # odd
                if total % 2:
                    return min(aR, bR)
                # even
                return (max(aL, bL) + min(aR, bR)) / 2
            elif aL > bR:
                r = a - 1
            else: # aR < bL
                l = a + 1
