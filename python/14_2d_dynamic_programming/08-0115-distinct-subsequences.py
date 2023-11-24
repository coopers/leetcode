class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        lil, big = (s, t) if len(s) < len(t) else (t, s)
        L, B = len(lil), len(big)
        dp = [0] * L
        for b in reversed(range(B)):
            prev = 1
            for l in reversed(range(L)):
                old_dpt = dp[l]
                if  lil[l] == big[b]:
                    dp[l] += prev

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

