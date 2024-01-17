from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        count = fleetTime = 0
        for p, s in pairs:
            time = (target - p) / s
            if not count or time > fleetTime:
                count += 1
                fleetTime = time

        return count


class Solution:
    def carFleet(self, target, pos, speed):
        time = [(target - p) / s for p, s in sorted(zip(pos, speed), reverse=True)]
        res = fleetTime = 0
        for t in time:
            if t > fleetTime:
                res += 1
                fleetTime = t
        return res





