from collections import defaultdict
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = defaultdict(list)
        for word in wordDict:
            words[len(word)].append(word)

        dp = [False] * n + [True]
        for i in reversed(range(n)):
            for l in words.keys():
                a = i + l
                if a <= n and dp[a] and any(word == s[i:a] for word in words[l]):
                    dp[i] = True
                    break

        return dp[0]


class Solution(object):
    def wordBreak(self, S, wordDict):
        WORDS = set(wordDict)
        MAX_WORD_LENGTH = max(len(word) for word in WORDS)
        MIN_WORD_LENGTH = min(len(word) for word in WORDS)
        N = len(S)
        dp = [False for _ in range(N + 1)]
        dp[0] = True
        for i in range(N):
            if dp[i]:
                for j in range(i + MIN_WORD_LENGTH, i + MAX_WORD_LENGTH):
                    if j == len(dp):
                        break
                    dp[j] = dp[j] or S[i:j] in WORDS
        return dp[-1]