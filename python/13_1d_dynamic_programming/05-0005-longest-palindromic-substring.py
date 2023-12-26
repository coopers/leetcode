class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for l, r in ((i,i), (i,i+1)): # odd and even sizes
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(res):
                        res = s[l:r + 1]
                    l -= 1
                    r += 1

        return res

# Manacher's Algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        c = r = 0
        for i in range(n):
            if i < r:
                p[i] = min(p[2 * c - i], r - i)

            while (
                i + 1 + p[i] < n and 
                i - 1 - p[i] >= 0 and
                t[i + 1 + p[i]] == t[i - 1 - p[i]]
            ):
                p[i] += 1

            if i + p[i] > r:
                c = i
                r = i + p[i]
                if r == n - 1:
                    break

        m = max(p)
        i = (p.index(m) - m) // 2
        j = i + m
        return s[i:j]
