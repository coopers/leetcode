class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        highest = height.index(max(height))
        for arr in [height[:highest], reversed(height[highest + 1:])]:
            nextHighest = 0
            for num in arr:
                if num < nextHighest:
                    volume += nextHighest - num
                else:
                    nextHighest = num
    
        return volume