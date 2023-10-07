from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]

        for i in reversed(range(len(s))):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    b = dp[i + len(w)]
                    if b:
                        dp[i] = True
                        break

        return dp[0]
