from collections import Counter


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if Counter(s1 + s2) != Counter(s3):
            return False

        if len(s2) > len(s1):
            s1, s2 = s2, s1
            
        m, n = len(s1), len(s2)
        dpPrev = [False] * (n + 1)
        for i in range(m, -1, -1):
            dp = [False] * (n + 1)
            for j in range(n, -1, -1):
                if (
                    (i == m and j == n) or
                    (i < m and s1[i] == s3[i + j] and dpPrev[j]) or
                    (j < n and s2[j] == s3[i + j] and dp[j + 1])
                ):
                    dp[j] = True
                    
            dpPrev = dp
        return dpPrev[0]