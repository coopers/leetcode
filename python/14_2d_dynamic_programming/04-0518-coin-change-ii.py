from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for n in range(coin, amount + 1):
                dp[n] += dp[n - coin]

        return dp[amount]