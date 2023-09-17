class Solution:
    def trap(self, height: List[int]) -> int:

        highest = height.index(max(height))
    
        volume = 0
        for arr in [height[:highest], reversed(height[highest + 1:])]:
            nextHighest = 0
            for num in arr:
                if num < nextHighest:
                    volume += nextHighest - num
                else:
                    nextHighest = num
    
        return volume