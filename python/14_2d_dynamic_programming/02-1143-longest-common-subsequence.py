class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        lil, big = (s1, s2) if len(s1) < len(s2) else (s2, s1)
        prev = [0] * (len(lil) + 1)
        curr = prev[:]
        for b in range(len(big) -1, -1, -1):
            for l in range(len(lil) -1, -1, -1):
                if big[b] == lil[l]:
                    curr[l] = 1 + prev[l + 1]
                else:
                    curr[l] = max(prev[l], curr[l + 1])
            prev, curr = curr, prev
        return prev[0]