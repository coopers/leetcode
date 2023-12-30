from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) -4, -1, -1):
            cost[i] += min(cost[i+1:i+3])
        
        return min(cost[:2])
