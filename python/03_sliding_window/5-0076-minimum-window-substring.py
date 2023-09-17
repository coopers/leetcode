from collections import Counter

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