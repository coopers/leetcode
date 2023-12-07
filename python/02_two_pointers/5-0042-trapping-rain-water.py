from typing import List



# Time   O(N)
# Space  O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lmax, rmax = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                if height[l] < lmax:
                    res += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if height[r] < rmax:
                    res += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1

        return res