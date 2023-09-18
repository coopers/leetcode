from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for j, curTemp in enumerate(temperatures):
            while stack and curTemp > stack[-1][1]:
                i, _ = stack.pop()
                res[i] = (j - i)
            stack.append((j, curTemp))
        return res