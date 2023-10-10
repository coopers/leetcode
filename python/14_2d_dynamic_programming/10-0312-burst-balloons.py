from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]

        for L in range(N - 2, 0, -1):
            for R in range(L, N - 1):
                for i in range(L, R + 1):
                    gain = nums[L - 1] * nums[i] * nums[R + 1]
                    remaining = dp[L][i - 1] + dp[i + 1][R]
                    dp[L][R] = max(remaining + gain, dp[L][R])
        return dp[1][N - 2]