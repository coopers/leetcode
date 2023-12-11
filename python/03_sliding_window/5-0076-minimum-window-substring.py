from collections import Counter
from collections import defaultdict
import math



# Time   O(LS + LT)
# Space  O(LS + LT)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        counter = defaultdict(int)
        for ch in t:
            counter[ch] -= 1

        need = len(counter)
        resL = resR = resLen = math.inf
        l = 0
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] += 1
                if counter[s[r]] == 0:
                    need -= 1
                while need == 0:
                    strLen = r - l + 1
                    if strLen < resLen:
                        resL, resR, resLen = l, r, strLen
                    if s[l] in counter:
                        counter[s[l]] -= 1
                        if counter[s[l]] < 0:
                            need += 1
                    l += 1

        return '' if resLen == math.inf else s[resL:resR + 1]
