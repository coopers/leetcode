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
    def isMatch(self, s_str: str, p_str: str) -> bool:
        S, P = len(s_str), len(p_str)
        cache = {}

        def dfs(s, p):
            if (s, p) in cache:
                return cache[(s, p)]
            if s >= S and p >= P:
                return True
            if p >= P:
                return False

            match = s < S and (s_str[s] == p_str[p] or p_str[p] == ".")
            if (p + 1) < P and p_str[p + 1] == "*":
                cache[(s, p)] = dfs(s, p + 2) or (match and dfs(s + 1, p))
                return cache[(s, p)]
            if match:
                cache[(s, p)] = dfs(s + 1, p + 1)
                return cache[(s, p)]
            cache[(s, p)] = False
            return False

        return dfs(0, 0)