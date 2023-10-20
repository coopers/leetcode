from typing import List



class Solution:
    def carFleet(self, target, pos, speed):
        time = [(target - p) / s for p, s in sorted(zip(pos, speed), reverse=True)]
        res = cur = 0
        for t in time:
            if t > cur:
                res += 1
                cur = t
        return res




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



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionsAndDurations = [(position[i], (target - position[i]) / speed[i]) 
                            for i in range(len(speed))]
        positionsAndDurations.sort()
        numFleets = 0
        blocker = None
        while positionsAndDurations:
            _, duration = positionsAndDurations.pop()
            if blocker is None or duration > blocker:
                numFleets += 1
                blocker = arrival
        return numFleets
    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionsAndDurations = [(position[i], (target - position[i]) / speed[i]) 
                            for i in range(len(speed))]
        positionsAndDurations.sort()
        stack = []
        while positionsAndDurations:
            _, duration = positionsAndDurations.pop()
            if not stack or duration > stack[-1]:
                stack.append(duration)
        return len(stack)