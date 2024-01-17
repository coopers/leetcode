from typing import List



# Time   O(N)
# Space  O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for right, short in enumerate(heights):
            left = right
            while stack and short < stack[-1][0]:
                tall, left = stack.pop()
                largest = max(largest, tall * (right - left))
            
            stack.append((short, left))
        
        remaining = max(h * (len(heights) - i) for h, i in stack)
        return max(largest, remaining)
