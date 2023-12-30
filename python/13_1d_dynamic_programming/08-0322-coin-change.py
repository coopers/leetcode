from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        return -1 if dp[amount] == math.inf else dp[amount]

