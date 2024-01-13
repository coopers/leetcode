class Solution:
    def numDistinct(self, s_str: str, t_str: str) -> int:
        S, T = len(s_str), len(t_str)
        if S < T:
            return 0
        
        prev = None
        for s in range(S, -1, -1):
            curr = [0] * (T+1)
            for t in range(T, -1, -1):
                if t == T:
                    curr[t] = 1
                elif s == S:
                    curr[t] = 0
                elif s_str[s] == t_str[t]:
                    curr[t] = prev[t+1] + prev[t]
                else:
                    curr[t] = prev[t]

            prev = curr
        return prev[0]


class Solution:
    def numDistinct(self, s_str: str, t_str: str) -> int:
        S, T = len(s_str), len(t_str)
        if S < T:
            return 0

        cache = {}
        def helper(s, t):
            if t == T:
                return 1
            
            if s == S:
                return 0
            
            if (s, t) in cache:
                return cache[(s, t)]

            if s_str[s] == t_str[t]:
                cache[(s, t)] = helper(s+1, t+1) + helper(s+1, t)
            else:
                cache[(s, t)] = helper(s+1, t)

            return cache[(s, t)]
        
        return helper(0, 0)


