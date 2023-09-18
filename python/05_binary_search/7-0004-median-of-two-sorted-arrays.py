from typing import List


# Time: log(min(n, m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1
        while True:
            a = l + (r - l) // 2
            b = half - a - 2
            a_L = A[a] if a >= 0 else float("-infinity")
            b_L = B[b] if b >= 0 else float("-infinity")
            a_R = A[a + 1] if (a + 1) < len(A) else float("infinity")
            b_R = B[b + 1] if (b + 1) < len(B) else float("infinity")
            # partition is correct
            if a_L <= b_R and b_L <= a_R:
                # odd
                if total % 2:
                    return min(a_R, b_R)
                # even
                return (max(a_L, b_L) + min(a_R, b_R)) / 2
            elif a_R < b_L:
                l = a + 1
            else:
                r = a - 1
