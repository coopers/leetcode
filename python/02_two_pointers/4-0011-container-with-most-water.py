class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            if height[l] < height[r]:
                area = max(area, height[l] * width)
                l += 1
            else:
                area = max(area, height[r] * width)
                r -= 1
        return area