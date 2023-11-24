class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        lil, big = (s1, s2) if len(s1) < len(s2) else (s2, s1)
        L, B = len(lil), len(big)
        prev = [False] * (L + 1)
        for b in range(B, -1, -1):
            curr = [False] * (L + 1)
            for l in range(L, -1, -1):
                if (
                    (l == L and b == B) or
                    (l < L and curr[l + 1] and lil[l] == s3[l + b]) or
                    (b < B and prev[l] and big[b] == s3[l + b])
                ):
                    curr[l] = True
                    
            prev = curr
        return prev[0]