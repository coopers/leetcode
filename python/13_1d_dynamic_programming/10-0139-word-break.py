from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    j = i + len(w)
                    if j <= n and not dp[j]:
                        dp[j] = s[i:j] == w

        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        words = defaultdict(set)
        for w in wordDict:
            words[len(w)].add(w)
            
        word_lengths = list(words.keys())
        word_lengths.sort()
        for i in range(n):
            if dp[i]:
                for l in word_lengths:
                    j = i + l
                    if j <= n and not dp[j] and s[i:j] in words[l]:
                        dp[j] = True

        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) 
        dp[len(s)] = True
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and dp[i + len(w)] and s[i : i + len(w)] == w:
                    dp[i] = True
                    break

        return dp[0]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        def helper(i, w):
            j = i + len(w)
            return j <= len(s) and dp[j] and w == s[i:j]
        
        for i in range(len(dp) -2, -1, -1):
            dp[i] = any(helper(i, w) for w in wordDict)

        return dp[0]