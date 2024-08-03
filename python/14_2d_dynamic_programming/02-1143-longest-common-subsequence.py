class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        lil, big = (s, t) if len(s) < len(t) else (t, s)
        L, B = len(lil), len(big)
        prev = [0] * (L + 1)
        for b in range(B):
            curr = [0] * (L + 1)
            for l in range(L):
                if lil[l] == big[b]:
                    curr[l + 1] = 1 + prev[l]
                else:
                    curr[l + 1] = max(curr[l], prev[l + 1])
            prev = curr
        
        return prev[-1]
    
text1 = "abcde"
text2 = "ace"
assert Solution().longestCommonSubsequence(text1, text2) == 3