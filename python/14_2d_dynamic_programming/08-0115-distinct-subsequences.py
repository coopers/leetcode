class Solution:
    def numDistinct(self, big_str: str, lil_str: str) -> int:
        L, B = len(lil_str), len(big_str)
        if L > B:
            return 0
        
        dp = [0] * L
        for b in reversed(range(B)):
            prev = 1
            for l in reversed(range(L)):
                old_dpt = dp[l]
                if  lil_str[l] == big_str[b]:
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

