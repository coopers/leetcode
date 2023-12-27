from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        def helper(i, w):
            j = i + len(w)
            return j <= len(s) and dp[j] and w == s[i:j]
        
        for i in range(len(dp) -2, -1, -1):
            dp[i] = any(helper(i, w) for w in wordDict)

        return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        for i in range(len(dp) -2, -1, -1):
            for w in wordDict:
                j = i + len(w)
                if j <= len(s) and dp[j] and w == s[i:j]:
                    dp[i] = True
                    break

        return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]