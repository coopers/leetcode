class Solution:
    def numDistinct(self, s_str: str, t_str: str) -> int:
        S, T = len(s_str), len(t_str)
        dp = [0] * T
        prev = None
        for s in reversed(range(S)):
            prev = 1
            for t in reversed(range(T)):
                old_dpt = dp[t]
                if s_str[s] == t_str[t]:
                    dp[t] += prev

                prev = old_dpt

        return dp[0]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]

