from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for n in range(coin, amount + 1):
                dp[n] += dp[n - coin]

        return dp[amount]