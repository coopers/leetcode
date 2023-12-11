from typing import List



# Time   O(N)
# Space  O(N)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (height, index)

        for right, short in enumerate(heights):
            start = right
            while stack and short < stack[-1][0]:
                tall, left = stack.pop()
                maxArea = max(maxArea, tall * (right - left))
                start = left
            stack.append((short, start))

        remaining = max(h * (len(heights) - i) for h, i in stack)
        return max(maxArea, remaining)
