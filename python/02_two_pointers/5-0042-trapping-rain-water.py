from typing import List



# Time   O(N)
# Space  O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > lmax:
                    lmax = max(lmax, height[l])
                else:
                    res += lmax - height[l]
                l += 1
            else:
                if height[r] > rmax:
                    rmax = max(rmax, height[r])
                else:
                    res += rmax - height[r]
                r -= 1
        return res