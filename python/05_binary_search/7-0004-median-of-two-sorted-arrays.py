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
            aL = -math.inf if a < 0 else A[a]
            bL = -math.inf if b < 0 else B[b]
            aR = math.inf if (a + 1) == len(A) else A[a + 1]
            bR = math.inf if (b + 1) == len(B) else B[b + 1]
            # partition is correct
            if aL <= bR and bL <= aR:
                # odd
                if total % 2:
                    return min(aR, bR)
                # even
                return (max(aL, bL) + min(aR, bR)) / 2
            elif aR < bL:
                l = a + 1
            else:
                r = a - 1
