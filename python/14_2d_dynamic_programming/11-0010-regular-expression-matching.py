# BOTTOM-UP Dynamic Programming
class Solution:
    def isMatch(self, s_str: str, p_str: str) -> bool:
        S, P = len(s_str), len(p_str)
        dp = [[False] * (P + 1) for _ in range(S + 1)]
        dp[S][P] = True

        for s in reversed(range(S + 1)):
            for p in reversed(range(P)):
                match = s < S and p_str[p] in (s_str[s], '.')

                if (p + 1) < P and p_str[p + 1] == "*":
                    dp[s][p] = dp[s][p + 2]
                    if match:
                        dp[s][p] = dp[s + 1][p] or dp[s][p]
                elif match:
                    dp[s][p] = dp[s + 1][p + 1]

        return dp[0][0]


# TOP DOWN MEMOIZATION
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (  # dont use *
                    match and dfs(i + 1, j)
                )  # use *
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)