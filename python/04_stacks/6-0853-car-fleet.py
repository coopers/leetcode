from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:  # Reverse Sorted Order By Position
            stack.append((target - p) / s) # Time to target
            if len(stack) > 1 and stack[-1] <= stack[-2]: # Second car in fleet
                stack.pop()
        return len(stack)
