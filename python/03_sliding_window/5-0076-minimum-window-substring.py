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
                if not counter[s[r]]:
                    need -= 1
                while not need:
                    strLen = r - l + 1
                    if strLen < resLen:
                        resL, resR, resLen = l, r, strLen
                    if s[l] in counter:
                        counter[s[l]] -= 1
                        if counter[s[l]] < 0:
                            need += 1
                    l += 1

        return '' if resLen == math.inf else s[resL:resR + 1]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        window = {}
        have, need = 0, len(counter)
        resLeft = resRight = resLen = None
        l = 0
        for r, ch in enumerate(s):
            window[ch] = 1 + window.get(ch, 0)
            if ch in counter and window[ch] == counter[ch]:
                have += 1

            while have == need:
                strLen = r - l + 1
                if resLen is None or strLen < resLen:
                    resLeft, resRight, resLen = l, r, strLen
                window[s[l]] -= 1
                if s[l] in counter and window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1
        
        return s[resLeft:resRight + 1] if resLen else ""