from typing import List



# Time   O(N)
# Space  O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        while l < r:
            if lmax < rmax:
                res += (lmax - height[l])
                l += 1
                lmax = max(lmax, height[l])
            else:
                res += (rmax - height[r])
                r -= 1
                rmax = max(rmax, height[r])
        
        return res