class Solution:
    def characterReplacement(self, s, k):
        counter = {}
        maxf = 0
        l = 0
        for r, ch in enumerate(s):
            counter[ch] = 1 + counter.get(ch, 0)
            maxf = max(maxf, counter[ch])
            if maxf + k < r - l + 1:
                counter[s[l]] -= 1
                l += 1

        return len(s) - l