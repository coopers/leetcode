from typing import List
import math


# Time: log(min(n, m))
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half, isOdd = divmod(total, 2)
        l, r = 0, len(A) - 1
        while True:
            a = l + (r - l) // 2
            b = half - a - 2
            aL = -math.inf if a < 0 else A[a]
            bL = -math.inf if b < 0 else B[b]
            aR = math.inf if (a + 1) == len(A) else A[a + 1]
            bR = math.inf if (b + 1) == len(B) else B[b + 1]
            if aL <= bR and bL <= aR:
                if isOdd:
                    return min(aR, bR)
                else:
                    return (min(aR, bR) + max(aL, bL)) / 2
            elif aR < bL:
                l = a + 1
            else:
                r = a - 1

A = []
B = [1]
assert Solution().findMedianSortedArrays(A, B) == 1