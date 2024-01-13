class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m

        dp = [1] * m
        for _ in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i-1]
        return dp[-1]
    
assert Solution().uniquePaths(3, 7) == 28