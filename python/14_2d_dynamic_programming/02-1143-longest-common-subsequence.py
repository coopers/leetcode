class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        lil, big = (s, t) if len(s) < len(t) else (t, s)
        L, B = len(lil), len(big)
        prev = [0] * (L + 1)
        for b in reversed(range(B)):
            curr = [0] * (L + 1)
            for l in reversed(range(L)):
                if lil[l] == big[b]:
                    curr[l] = 1 + prev[l + 1]
                else:
                    curr[l] = max(curr[l + 1], prev[l])
            prev = curr
        
        return prev[0]
    
text1 = "abcde"
text2 = "ace"
assert Solution().longestCommonSubsequence(text1, text2) == 3