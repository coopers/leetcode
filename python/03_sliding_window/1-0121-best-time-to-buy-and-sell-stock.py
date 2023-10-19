from typing import List
import math



# Time   O(N)
# Space  O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = math.inf
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = max(profit, price - lowest)
        
        return profit
