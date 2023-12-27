import math


class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        c = r = 0
        p = [0] * n
        for i in range(n):
            if i < r:
                p[i] = min(p[2 * c - i], r - i)

            while (
                i - p[i] - 1 >= 0 and
                i + p[i] + 1 < n and
                t[i - p[i] - 1] == t[i + p[i] + 1]
            ):
                p[i] += 1
            
            if r < i + p[i]:
                c = i
                r = p[i] + i
        
        return sum(math.ceil(n / 2) for n in p)


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for l, r in ((i,i), (i,i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1

        return count