class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lil, big = (word1, word2) if len(word1) < len(word2) else (word2, word1)
        L, B = len(lil), len(big)
        prev = None
        for b in range(B, -1, -1):
            curr = [0] * (L+1)
            for l in range(L, -1, -1):
                if b == B:
                    curr[l] = L - l
                elif l == L:
                    curr[l] = B - b
                elif lil[l] == big[b]:
                    curr[l] = prev[l + 1]
                else:
                    curr[l] = 1 + min(curr[l + 1], prev[l], prev[l + 1])
            
            prev = curr
        return prev[0]

assert Solution().minDistance("horse", "ros") == 3
assert Solution().minDistance("intention", "execution") == 5

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         if not len(word1) or not len(word2):
#             return len(word1) or len(word2) or 0
    
#         dp = [[math.inf] * (len(word2) + 1) for _ in range(len(word1) + 1)]
#         for i in range(len(word1) + 1):
#             dp[i][len(word2)] = len(word1) - i
#         for j in range(len(word2) + 1):
#             dp[len(word1)][j] = len(word2) - j

#         for i in range(len(word1) -1, -1, -1):
#             for j in range(len(word2) -1, -1, -1):
#                 if word1[i] == word2[j]:
#                     dp[i][j] = dp[i+1][j+1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        
#         return dp[0][0]
