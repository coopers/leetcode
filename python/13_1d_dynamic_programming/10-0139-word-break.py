from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        words = set(wordDict)
        for i in reversed(range(len(s))):
            if :
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